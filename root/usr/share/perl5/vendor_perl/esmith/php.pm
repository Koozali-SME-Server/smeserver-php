package esmith::php;

use strict;
use warnings;
use esmith::ConfigDB;

our $PHPDEFAULT = 82;
our $BASEPHP = 81;

our @ISA = qw(Exporter);
our @EXPORT = qw( listPHPVersionFPM listPHPVersionShort listPHPVersionHash listPHPVersionHashShort  PHPdefault PHPbase VersionToUse  PhpFpmVersionToUse  $defaultdisabledfunc %defaultPHPproperties);

our $defaultdisabledfunc='system,show_source,' .
        'symlink,exec,dl,shell_exec,' .
        'passthru,phpinfo,' .
        'escapeshellarg,escapeshellcmd';
my $configdb = esmith::ConfigDB->open_ro or die "Could not open accounts db";
our %defaultPHPproperties = (
        MemoryLimit       => '128M',
        MaxExecutionTime  => '30',
        MaxInputTime      => '60',
        AllowUrlFopen     => 'disabled',
        PostMaxSize       => '20M',
        UploadMaxFilesize => '10M',
        FileUpload        => 'enabled',
        PHPBaseDir        => '/home/e-smith/files/ibays/$key:/var/lib/php/$key',
        DisabledFunctions => $defaultdisabledfunc,
        MailForceSender   => "admin@".$configdb->get_value('DomainName'),
        AllowPHTML        => 'disabled',
	AutoPrependFile	  => 'enabled',
);

=head1 NAME

esmith::php - A few tools to help with php-fpm installed versions

=head1 SYNOPSIS

    use esmith::php;

    my @phps=listPHPVersionFPM('enabled');

=head1 DESCRIPTION

This is intended to help playing with installed php versions.

=head1 Methods


=head2 listPHPVersionFPM
param = (enabled, disabled, all) , if empty default to all
this will return you an array of php-fpm versions available php version
print "'$_'\n" for listPHPVersionFPM('all');
'php-fpm'
'php72-php-fpm'
'php73-php-fpm'
'php74-php-fpm'
'php80-php-fpm'
'php81-php-fpm'
'php82-php-fpm'
'php83-php-fpm'

this will return only available and enabled
print "'$_'\n" for listPHPVersionFPM('enabled');
=cut
sub listPHPVersionFPM {
  my $status = shift  || 'all';
  my $conf = esmith::ConfigDB->open_ro or die "Could not open accounts db";
  my @list = $conf->get_all_by_prop( type => 'service' );
  my @keys = map {$_->key; } @list;
  my @FPM;
  foreach my $service (  grep(/^(php[0-9]{2}-)?php-fpm$/,@keys) ) {
    my $s = $conf->get($service);
    next unless ($s) ;
    next unless (-f "/usr/lib/systemd/system/$service.service") ;
    next unless ( $status eq "all" || ($s->prop('status') || "disabled") eq $status );
    push @FPM, $service;
  }
 return @FPM
}

=head2 listPHPVersionShort
param1 = (enabled, disabled, all) , if empty default to all
param2 = will use "" as output for base php

this will return you an array of numerical available php version
print "'$_'\n" for listPHPVersionShort('all');
'72'
'73'
'74'
'80'
'81'
'82'
'83'

this will returnonly available and enabled
print "'$_'\n" for listPHPVersionShort('enabled');
=cut
sub listPHPVersionShort {
  my $status = shift  || 'all';
  my $emptyforbase = shift;
  my @FPM = listPHPVersionFPM($status);
  s/^php([0-9]{2})-php-fpm$/$1/ for @FPM ;
  my $base= (defined $emptyforbase) ? "" : $BASEPHP;
  s/^php-fpm$/$base/ for @FPM ;
  return @FPM;
}

=head2 listPHPVersionHash
param1 = (enabled, disabled, all) , if empty default to all
param2 = if defined will use "" as key for php-fpm
this will return you a hash order by version 
my %list= listPHPVersionHash();
print "$_ => $list{$_}\n" for (sort keys %list);
72 => php72-php-fpm
73 => php73-php-fpm
74 => php74-php-fpm
80 => php80-php-fpm
81 => php81-php-fpm
82 => php82-php-fpm
83 => php83-php-fpm

=cut
sub listPHPVersionHash {
  my $status = shift  || 'all';
  my $emptyforbase = shift;
  my @FPM = listPHPVersionFPM($status);
  my %myfpm;
  my $base= (defined $emptyforbase) ? "" : $BASEPHP;
  for my $php ( @FPM)  {
    $myfpm{$base}="$php" for ( $php=~/^php-fpm$/);
    $myfpm{$_}="$php"  for ( $php=~/^php([0-9]{2})-php-fpm$/);
  }
  return %myfpm;
}

=head2 listPHPVersionHashShort
param1 = (enabled, disabled, all) , if empty default to all
param2 = if defined will use "" as key for php-fpm

this will return you a hash order by version 
my %list= listPHPVersionHashShort();
print "$_ => $list{$_}\n" for (sort keys %list);
72 => php72
73 => php73
74 => php74
80 => php80
81 => php81
82 => php82
83 => php83

=cut
sub listPHPVersionHashShort {
  my $status = shift  || 'all';
  my $emptyforbase = shift;
  my %myfpm = listPHPVersionHash($status,  $emptyforbase);
  my %rfpm;
  foreach my $key (keys %myfpm) {
    my $php = $myfpm{$key};
    ($rfpm{$key}=  $php)=~s/(^php[0-9]{0,2}).*/$1/;
  }
  return %rfpm;
}

=head2 PHPdefault
 return the php default version for the system, i.e. default chosen by rpm or the one overrided by the admin in php PHPVersion property.
 one optional argument is to display 54 as empty string (i.e. base php-fpm)

=cut
sub PHPdefault {
  my $emptyforbase = shift;
  my $conf = esmith::ConfigDB->open_ro or die "Could not open accounts db";
  my $php = $conf->get('php') ;
  my $PHPVersion = ( defined $php->prop('PHPVersion') ) ? $php->prop('PHPVersion') : $PHPDEFAULT;
  $PHPVersion = ($PHPVersion eq "") ? $BASEPHP : $PHPVersion;
  $PHPVersion = ($PHPVersion =~ /([0-9]{2})/) ? $1 : $PHPDEFAULT;
  return $PHPVersion unless defined $emptyforbase;
  $PHPVersion = ( $PHPVersion eq $BASEPHP ) ? "" : $PHPVersion; 
  return $PHPVersion;
}

=head2 PHPbase
return the php base, i.e. 54 for php-fpm provided by CentOS 7.

=cut
sub PHPbase {
  return $BASEPHP; 
}

=head2 VersionToUse
argument 1 : output from $account->get('ibayname') or similar (shares,custom)
 it is expected to find in this entry a property PHPVersion
artgument 2 : optional, a locally forced PHP version, if you do not want to trust globally prefered one. 

output : a two digit php version : 74 for php 7.4 . 54 will be for php-fpm 5.4 as default php on CentOS 7 /SME 9

 my $ibay=$account->get('ibayname');
 my $version = VersionToUse($ibay,'80');

logic:
# if not defined => $PHPDEFAULT
# if defined and empty strin => $BASEPHP
# if defined and not empty  => its value

# defined entry (e.g. ibay)  PHPVersion property  override 
  - defined forced PHPVersion provided (2nd argument, if provided) which override
  - php PHPVersion property which override
  - default $PHPDEFAULT

=cut
sub VersionToUse {
  my $entry = shift or return "need a db entry";
  my $conf = esmith::ConfigDB->open_ro or die "Could not open accounts db";
 
  my $PHPVersion = PHPdefault();

  my $forcedefault = shift ;
  $forcedefault = ( defined $forcedefault ) ? $forcedefault : $PHPVersion; 
  $forcedefault = ($forcedefault eq "") ? $BASEPHP : $forcedefault;
  $forcedefault = ($forcedefault =~ /([0-9]{2})/) ? $1 : $PHPVersion;

  my $entryPHPVersion = (defined $entry->prop('PHPVersion') ) ? $entry->prop('PHPVersion') : $forcedefault;
  $entryPHPVersion = ($entryPHPVersion eq "") ? $BASEPHP : $entryPHPVersion;
  $entryPHPVersion = ($entryPHPVersion =~ /([0-9]{2})/) ? $1 : $forcedefault;

  # we currently assume that it is installed and enabled, but could test it here
  
  my $version= $entryPHPVersion ;
  #$version = " $PHPDEFAULT - $PHPVersion - $forcedefault - $entryPHPVersion";

 return $version;
}

=head2 PhpFpmVersionToUse
same as VersionToUse except it will return null string in place of $BASEPHP  (i.e.  "" in place of 54)

argument 1 : output from $account->get('ibayname') or similar (shares,custom)
 it is expected to find in this entry a property PHPVersion
artgument 2 : optional, a locally forced PHP version, if you do not want to trust globally prefered one. 

output : a two digit php version : 74 for php 7.4  or empty string, as '' will take place of 54 for php-fpm 5.4 as default php on CentOS 7 /SME 9

=cut 
sub PhpFpmVersionToUse {
  #my $entry = shift or return "need a db entry";
  #my $forcedefault = shift ;
  my $version ;
  $version = VersionToUse(@_) ;#$entry,$forcedefault);# if defined $forcedefault;
  #$version = VersionToUse($entry) unless defined $forcedefault;
  # here we convert $BASEPHP to empty string
  $version = ( $version eq $BASEPHP ) ? "" : $version;
  return $version;
}
