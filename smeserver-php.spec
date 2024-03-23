%define version 3.0.0
%define release 49
%define name smeserver-php


Summary: PHP FPM pools and more on SME Server
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: MIT
Group: Applications/System
Source: %{name}-%{version}.tar.xz

BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArch: x86_64
BuildRequires: e-smith-devtools

Requires: e-smith-base >= 5.6.0
Provides: e-smith-php = %{version}-%{release}
Obsoletes: e-smith-php < %{version}
Provides: smeserver-webapps-common
Provides: php(language) = 7.0
Provides: php(language) = 7.1
Provides: php(language) = 7.2
Provides: php(language) = 7.3
Provides: php(language) = 7.4
Provides: php(language) = 8.0
Provides: php(language) = 8.1
Provides: php(language) = 8.2
Provides: php(language) = 8.3
Requires: tmpwatch
Requires: logrotate

# Stock PHP
Requires: php-cli
Requires: php-ldap
Requires: php-imap
Requires: php-gd
Requires: php-xml
Requires: php-xmlrpc
Requires: php-soap
Requires: php-opcache
Requires: php-fpm
Requires: php-mbstring
Requires: php-mysql
Requires: php-json
Requires: php-bcmath
Requires: php-intl
Requires: php-mcrypt
Requires: php-pear
Requires: php-process
Requires: php-snmp


# PHP 5.5
Requires: php55-php-cli
Requires: php55-php-ldap
Requires: php55-php-imap
Requires: php55-php-gd
Requires: php55-php-xml
Requires: php55-php-xmlrpc
Requires: php55-php-soap
Requires: php55-php-opcache
Requires: php55-php-fpm
Requires: php55-php-mbstring
Requires: php55-php-mysql
Requires: php55-php-json
Requires: php55-php-bcmath
Requires: php55-php-intl
Requires: php55-php-mcrypt
Requires: php55-php-pear
Requires: php55-php-process
Requires: php55-php-snmp
Requires: php55-php, php55-php-enchant , php55-php-pdo php55-php-tidy ,  php55-php-mysqlnd php55-php-pecl-zip

# PHP 5.6
Requires: php56-php-cli
Requires: php56-php-ldap
Requires: php56-php-imap
Requires: php56-php-gd
Requires: php56-php-xml
Requires: php56-php-xmlrpc
Requires: php56-php-soap
Requires: php56-php-opcache
Requires: php56-php-fpm
Requires: php56-php-mbstring
Requires: php56-php-mysql
Requires: php56-php-json
Requires: php56-php-bcmath
Requires: php56-php-intl
Requires: php56-php-mcrypt
Requires: php56-php-pear
Requires: php56-php-process
Requires: php56-php-snmp
Requires: php56-php, php56-php-enchant , php56-php-pdo php56-php-tidy ,  php56-php-mysqlnd php56-php-pecl-zip

# PHP 7.0
Requires: php70-php-cli
Requires: php70-php-ldap
Requires: php70-php-imap
Requires: php70-php-gd
Requires: php70-php-xml
Requires: php70-php-xmlrpc
Requires: php70-php-soap
Requires: php70-php-opcache
Requires: php70-php-fpm
Requires: php70-php-mbstring
Requires: php70-php-mysql
Requires: php70-php-json
Requires: php70-php-bcmath
Requires: php70-php-intl
Requires: php70-php-mcrypt
Requires: php70-php-pear
Requires: php70-php-process
Requires: php70-php-snmp
Requires: php70-php, php70-php-enchant , php70-php-pdo php70-php-tidy ,  php70-php-mysqlnd php70-php-pecl-zip

# PHP 7.1
Requires: php71-php-cli
Requires: php71-php-ldap
Requires: php71-php-imap
Requires: php71-php-gd
Requires: php71-php-xml
Requires: php71-php-xmlrpc
Requires: php71-php-soap
Requires: php71-php-opcache
Requires: php71-php-fpm
Requires: php71-php-mbstring
Requires: php71-php-mysql
Requires: php71-php-json
Requires: php71-php-bcmath
Requires: php71-php-intl
Requires: php71-php-mcrypt
Requires: php71-php-pear
Requires: php71-php-process
Requires: php71-php-snmp
Requires: php71-php, php71-php-enchant , php71-php-pdo php71-php-tidy ,  php71-php-mysqlnd php71-php-pecl-zip

# PHP 7.2
Requires: php72-php-cli
Requires: php72-php-ldap
Requires: php72-php-imap
Requires: php72-php-gd
Requires: php72-php-xml
Requires: php72-php-xmlrpc
Requires: php72-php-soap
Requires: php72-php-opcache
Requires: php72-php-fpm
Requires: php72-php-mbstring
Requires: php72-php-mysql
Requires: php72-php-json
Requires: php72-php-bcmath
Requires: php72-php-intl
Requires: php72-php-mcrypt
Requires: php72-php-pear
Requires: php72-php-process
Requires: php72-php-snmp
Requires: php72-php, php72-php-enchant , php72-php-pdo php72-php-tidy ,  php72-php-mysqlnd php72-php-pecl-zip

# PHP 7.3
Requires: php73-php-cli
Requires: php73-php-ldap
Requires: php73-php-imap
Requires: php73-php-gd
Requires: php73-php-xml
Requires: php73-php-xmlrpc
Requires: php73-php-soap
Requires: php73-php-opcache
Requires: php73-php-fpm
Requires: php73-php-mbstring
Requires: php73-php-mysql
Requires: php73-php-json
Requires: php73-php-bcmath
Requires: php73-php-intl
Requires: php73-php-pear
Requires: php73-php-process
Requires: php73-php-snmp
Requires: php73-php, php73-php-enchant , php73-php-pdo php73-php-tidy ,  php73-php-mysqlnd php73-php-pecl-zip

# PHP 7.4
Requires: php74-php-cli
Requires: php74-php-ldap
Requires: php74-php-imap
Requires: php74-php-gd
Requires: php74-php-xml
Requires: php74-php-xmlrpc
Requires: php74-php-soap
Requires: php74-php-opcache
Requires: php74-php-fpm
Requires: php74-php-mbstring
Requires: php74-php-json
Requires: php74-php-bcmath
Requires: php74-php-intl
Requires: php74-php-pear
Requires: php74-php-process
Requires: php74-php-snmp
Requires: php74-php, php74-php-enchant , php74-php-pdo php74-php-tidy ,  php74-php-mysqlnd php74-php-pecl-zip

# PHP 8.0
Requires: php80-php-cli
Requires: php80-php-ldap
Requires: php80-php-imap
Requires: php80-php-gd
Requires: php80-php-xml
Requires: php80-php-xmlrpc
Requires: php80-php-soap
Requires: php80-php-opcache
Requires: php80-php-fpm
Requires: php80-php-mbstring
Requires: php80-php-json
Requires: php80-php-bcmath
Requires: php80-php-intl
Requires: php80-php-pear
Requires: php80-php-process
Requires: php80-php-snmp
Requires: php80-php, php80-php-enchant , php80-php-pdo php80-php-tidy ,  php80-php-mysqlnd php80-php-pecl-zip

# PHP 8.1
Requires: php81-php-cli
Requires: php81-php-ldap
Requires: php81-php-imap
Requires: php81-php-gd
Requires: php81-php-xml
Requires: php81-php-xmlrpc
Requires: php81-php-soap
Requires: php81-php-opcache
Requires: php81-php-fpm
Requires: php81-php-mbstring
Requires: php81-php-json
Requires: php81-php-bcmath
Requires: php81-php-intl
Requires: php81-php-pear
Requires: php81-php-process
Requires: php81-php-snmp
Requires: php81-php, php81-php-enchant , php81-php-pdo php81-php-tidy ,  php81-php-mysqlnd php81-php-pecl-zip

# PHP 8.2
Requires: php82-php-cli
Requires: php82-php-ldap
Requires: php82-php-imap
Requires: php82-php-gd
Requires: php82-php-xml
Requires: php82-php-xmlrpc
Requires: php82-php-soap
Requires: php82-php-opcache
Requires: php82-php-fpm
Requires: php82-php-mbstring
Requires: php82-php-json
Requires: php82-php-bcmath
Requires: php82-php-intl
Requires: php82-php-pear
Requires: php82-php-process
Requires: php82-php-snmp
Requires: php82-php, php82-php-enchant , php82-php-pdo php82-php-tidy ,  php82-php-mysqlnd php82-php-pecl-zip

# PHP 8.3
Requires: php83-php-cli
Requires: php83-php-ldap
Requires: php83-php-imap
Requires: php83-php-gd
Requires: php83-php-xml
Requires: php83-php-xmlrpc
Requires: php83-php-soap
Requires: php83-php-opcache
Requires: php83-php-fpm
Requires: php83-php-mbstring
Requires: php83-php-json
Requires: php83-php-bcmath
Requires: php83-php-intl
Requires: php83-php-pear
Requires: php83-php-process
Requires: php83-php-snmp
Requires: php83-php, php83-php-enchant , php83-php-pdo php83-php-tidy ,  php83-php-mysqlnd php83-php-pecl-zip

%description
Manage PHP FPM pools, and switch between PHP versions easily

%prep
%setup -q -n %{name}-%{version}

%build
perl createlinks
%{__mkdir_p} root/var/www/php-cgi-bin/
%{__mkdir_p} root/var/log/php/php/
%{__mkdir_p} root/var/lib/php/php/{session,tmp,opcache,wsdlcache}
#create service configuration for SME Seerver
#%{__mkdir_p} root/%{_unitdir}/php-fpm.service.d/
#echo '' >  root/%{_unitdir}/php-fpm.service.d/php-fpm.conf
#enable by default
#%{__mkdir_p} root/%{_presetdir}
#echo 'enable php-fpm.service' >root/%{_presetdir}/80-koozali-php.preset

#drop in systemd file
%{__mkdir_p} root/usr/lib/systemd/system/php-fpm.service.d
echo "[Install]" > root/usr/lib/systemd/system/php-fpm.service.d/51koozali.conf
echo "WantedBy=sme-server.target" >> root/usr/lib/systemd/system/php-fpm.service.d/51koozali.conf

%{__mkdir_p} root/etc/e-smith/templates.metadata/etc/logrotate.d/
for phpver in "55" "56" "70" "71" "72" "73" "74" "80" "81" "82" "83"; do
#needed folder
%{__mkdir_p} root/var/log/php/php$phpver/
%{__mkdir_p} root/var/lib/php/php$phpver/{session,tmp,opcache,wsdlcache}

#db configuration
%{__mkdir_p} root/etc/e-smith/db/configuration/defaults/php$phpver-php-fpm
%{__mkdir_p} root/etc/e-smith/db/configuration/defaults/php$phpver
echo 'enabled' > root/etc/e-smith/db/configuration/defaults/php$phpver-php-fpm/status
echo 'service'> root/etc/e-smith/db/configuration/defaults/php$phpver-php-fpm/type

echo 'configuration'> root/etc/e-smith/db/configuration/defaults/php$phpver/type
echo 'Off'> root/etc/e-smith/db/configuration/defaults/php$phpver/AllowUrlFopen

#logrotate templates
echo 'TEMPLATE_PATH="/etc/logrotate.d/php-fpm"
MORE_DATA={ PHP_VERSION => '$phpver'}' > root/etc/e-smith/templates.metadata/etc/logrotate.d/php$phpver-php-fpm

#drop in systemd file
%{__mkdir_p} root/usr/lib/systemd/system/php$phpver-php-fpm.service.d
echo "[Install]" > root/usr/lib/systemd/system/php$phpver-php-fpm.service.d/51koozali.conf
echo "WantedBy=sme-server.target" >> root/usr/lib/systemd/system/php$phpver-php-fpm.service.d/51koozali.conf
 
done

#to add a new php version
#php5*
for phpver in  "55" ; do
#cp php56 metadata
mkdir -p  root/etc/e-smith/templates.metadata/opt/remi/php$phpver
cp -a  root/etc/e-smith/templates.metadata/opt/remi/php56/* root/etc/e-smith/templates.metadata/opt/remi/php$phpver
#sed inplace
find root/etc/e-smith/templates.metadata/opt/remi/php$phpver  -type f -print0 | xargs -0 sed -i 's/56/'$phpver'/g'
done

# php7*
for phpver in  "72" "73" "74" "80" "81" "82" "83"; do
#cp ph70 metada
mkdir -p root/etc/e-smith/templates.metadata/etc/opt/remi/php$phpver/
cp -a  root/etc/e-smith/templates.metadata/etc/opt/remi/php70/* root/etc/e-smith/templates.metadata/etc/opt/remi/php$phpver/
#sed inplace
find root/etc/e-smith/templates.metadata/etc/opt/remi/php$phpver  -type f -print0 | xargs -0 sed -i 's/70/'$phpver'/g'
done

# then patch the following files
### TODO
### fix those files so we do not have to patch them, but generate them or sed them to change a known WORDTODOGENERIC
#smeserver-php-3.0.0/createlinks 
#smeserver-php-3.0.0/root/etc/e-smith/templates/etc/cron.daily/tmpwatch-php-fpm/10Defaults
#smeserver-php-3.0.0/root/etc/e-smith/templates/etc/logrotate.d/php-fpm/php-fpm 
#smeserver-php-3.0.0/root/etc/e-smith/templates/etc/rsyslog.conf/32php # this one could be cut in fragments per version
#smeserver-php-3.0.0/root/etc/e-smith/templates.metadata/etc/opt/remi/php81/php.ini

%install
/bin/rm -rf $RPM_BUILD_ROOT
(cd root; /usr/bin/find . -depth -print | /bin/cpio -dump $RPM_BUILD_ROOT)
/bin/rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
  --dir /var/log/php/php 'attr(0770,root,www)' \
  --dir /var/lib/php/php/session 'attr(0770,root,www)' \
  --dir /var/lib/php/php/tmp 'attr(0770,root,www)' \
  --dir /var/lib/php/php/opcache 'attr(0770,root,www)' \
  --dir /var/lib/php/php/wsdlcache 'attr(0770,root,www)' \
`for phpver in "54" "55" "56" "70" "71" "72" "73" "74" "80" "81" "82" "83"; do  echo -n "--dir /var/log/php/php$phpver attr(0770,root,www) --dir /var/lib/php/php$phpver/session attr(0770,root,www) --dir /var/lib/php/php$phpver/tmp attr(0770,root,www) --dir /var/lib/php/php$phpver/opcache attr(0770,root,www) --dir /var/lib/php/php$phpver/wsdlcache attr(0770,root,www) ";done `	\
  > %{name}-%{version}-filelist



%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%pre

%post
# %systemd_post %{pkgname}.service 

%preun

%changelog
* Sat Mar 23 2024 cvs2git.sh aka Brian Read <brianr@koozali.org> 3.0.0-49.sme
- Roll up patches and move to git repo [SME: 12338]

* Sat Mar 23 2024 BogusDateBot
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.

* Wed Mar 20 2024 Zsolt Vasarhelyi <vasarhelyizsolt@hotmail.com> 3.0.0-48.sme
- PHP 8.3 logs to 8.2 logdir [SME:12514]

* Mon Sep 04 2023 John Crisp <jcrisp@safeandsoundit.co.uk> 3.0.0-47.sme
- Add php83 support [SME:12405]

* Sat Aug 26 2023 John Crisp <jcrisp@safeandsoundit.co.uk>  3.0.0-46.sme
- fix missing php 81 settings
- Add php82 support [SME:12403]

* Sat Feb 04 2023 Jean-Philippe Pialasse <tests@pialasse.com> 3.0.0-45.sme
- fix session.save_handler forced without any way to change it [SME: 12303]

* Wed Dec 14 2022 Jean-Philippe Pialasse <tests@pialasse.com> 3.0.0-44.sme
- fix tkt auth not propagated to php pool [SME: 12269]

* Sun Apr 17 2022 Jean-Philippe Pialasse <tests@pialasse.com> 3.0.0-43.sme
- update to httpd 2.4 Require usage [SME: 11943]

* Mon Dec 20 2021 Jean-Philippe Pialasse <tests@pialasse.com> 3.0.0-42.sme
- fix missing section in php-fpm dropin file [SME: 11814]

* Sun Oct 24 2021 Jean-Philippe Pialasse <tests@pialasse.com> 3.0.0-41.sme
- add php81 support [SME: 11717]

* Fri Sep 24 2021 John Crisp <jcrisp@safeandsoundit.co.uk> 3.0.0-40.sme
- Fix incorrect commenting for error reporting

* Fri Sep 17 2021 Jean-Philippe Pialasse <tests@pialasse.com> 3.0.0-39.sme
- add ErrorReporting and DisplayErrors properties [SME: 8077]
  only per ibays (php defaults still hardcoded)
- fix typo in AllowUrlFopen, was using AllowUrlfOpen for ibays in httpd [SME: 11666]

* Wed Jun 30 2021 Jean-Philippe Pialasse <tests@pialasse.com> 3.0.0-37.sme
- fix typo in 25SSLDirectives fragment for WebAppVirtualHost [SME: 11641]

* Thu Jun 03 2021 Terry Fage <tfage@yahoo.com.au> 3.0.0-35.sme
- fix syntax error "> - >>" in spec file for systemd drop in [SME: 11612]

* Wed Apr 21 2021 Jean-Philippe Pialasse <tests@pialasse.com> 3.0.0-34.sme
- fix open_basedir for pool missing /var/lib/php/$ibay/ [SME: 11573]

* Tue Mar 16 2021 Jean-Philippe Pialasse <tests@pialasse.com> 3.0.0-33.sme
- clean rsyslog syntax for php [SME: 11422]

* Tue Mar 16 2021 Jean-Philippe Pialasse <tests@pialasse.com> 3.0.0-32.sme
- add /usr/share/pear and /usr/share/php to basedir [SME: 5759]
- fix last big differences between module setting and fpm [SME: 11452]

* Mon Mar 08 2021 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-31.sme
- move from e-smith-ibays handling of temps dirs [SME: 11412]
- improve httpd fragment [SME: 11401]

* Mon Mar 08 2021 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-30.sme
-  uniformize php related properties between ibays and php [SME: 11411]
   tidy fragments for php-fpm and ibays
-  revert patch for timeouts [SME: 11427]

* Mon Mar 08 2021 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-28.sme
- filter non existing php script [SME: 10907]
- allow php embded files per ibay using AllowPHTML [SME: 10890]
- add timeout property in case of need for long running script [SME: 11427]
  e.g. upgrade of a wiki

* Mon Mar 08 2021 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-27.sme
- String not honoured as php-fpm but as default [SME: 11401]

* Sat Mar 06 2021 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-26.sme
- improve sendmail parameter, force sender  [SME: 11410]
  MailForceSender as property for php versions, ibays and pools
- add perl module to help handling fpm version available [SME: 11413]

* Mon Feb 22 2021 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-25.sme
- add missing default db configuration for php80* [SME: 11378]

* Sun Feb 21 2021 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-24.sme
- allow php-pool-dirs to run from generik event [SME: 11287]
- add php80 support [SME: 11295]

* Wed Jan 27 2021 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-23.sme
- fix php55 logrotate [SME: 11325]
- cleanup remove services in sme-server.target.wants [SME: 10956]
- remove usr/lib preset file from rpm [SME: 10958]

* Fri Dec 25 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-22.sme
- add WantedBy=sme-server.target for all php-fpm service files [SME: 11294]

* Mon Dec 21 2020 John Crisp <jcrisp@safeandsoundit.co.uk> 3.0.0.21.sme
- Fix createlinks typo missing event links [SME: 11287]
- Fix typo

* Thu Dec 17 2020 John Crisp <jcrisp@safeandsoundit.co.uk> 3.0.0.20.sme
- Fix individual PHP version for ibay [SME: 11267]

* Sun Dec 13 2020 Jean-Philipe Pialasse <tests@pialasse.com.0.0-19.sme
- fix wrong syntax = in place of eq [SME: 11173]
  thanks to Terry Fage

* Mon Dec 07 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-18.sme
- fix logrotate error because parent directory has insecure permissions [SME: 11173]

* Wed Nov 18 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-17.sme
- fix warning: ~ action is deprecated with rsyslog [SME: 11015]
- fix logrotate error because parent directory has insecure permissions [SME: 11173]

* Mon Nov 09 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-16.sme
- fix typo for upload_tmp_dir [SME: 11092]

* Sun Nov 08 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-15.sme
- improve integration of webapps : virtualhost and event [SME: 11087]

* Wed Sep 30 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-14.sme
- enable php services for sme-server.target [SME: 11014]

* Tue Jun 23 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-13.sme
- move and fix link to start services units [SME: 10960]

* Fri Mar 27 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-12.sme
- fix typo in  smeserver-php-3.0.0-bz10904-pass-auth-token-to-fpm.patch [SME: 10904]

* Thu Mar 26 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-11.sme
- help monitoring email sent by php [SME: 8787]

* Thu Mar 26 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-9.sme
- move auto_prepend_file from php.ini to php-fpm.d [SME: 10904]
  add /usr/share/php in open_basedir if dfined to allow execution of auto_prepend_file
- fix templates-metadata path fot php 55 72 73 74

* Tue Mar 24 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-8.sme
- transfer SERVER auth variables from httpd server to php-fpm pool [SME: 10904]
  this allow easy auth for php app using httpd auth as if using php module

* Tue Mar 24 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-7.sme
- templating all php.ini for all available version [SME: 10891]
  expanded using webapps-update, smeserver-php-update, console-save and bootstrap-console-save
  Values are those from php configuration key, unless defined for the php$VERSION key.
  only one template for all, using templates.metadata and conditions vhen needed. 
  reworked the content of the php.ini to have it uptodate

* Wed Mar 11 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-6.sme
- enable units for php-fpm services [SME: 10335]

* Tue Mar 10 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-5.sme
- set sys_temp_dir for php-fpm and ibays [SME: 10888]
- set restart for php-fpm services in the smeserver-php-update event  [SME: 10335]

* Mon Mar 09 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-3.sme
- fix typos and logic in scripts [SME: 10335]
- only set php admin values if php module is enabled [SME: 10871]
- redirect php*-php-fpm services logs to /var/log/php/php*/php-fpm.log [SME: 10879]
- pool logs in /var/log/php/*/error.log [SME: 10877] 

* Sat Feb 01 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-2.sme
- modification for ibays php-fpm support in httpd.conf [SME: 10871]

* Tue Jan 28 2020 Jean-Philipe Pialasse <tests@pialasse.com> 3.0.0-1.sme
- initial release of smeserver-php from smeserver-php-fpm [SME: 10335]
  added support for ibays, remove references to shares (should move to smeserver-share-folders)
- merge and Obsoletes e-smith-php [SME: 10335]
- remove reference to php3 and php4 files [SME: 10865]

* Thu Jul 27 2017 Daniel Berteaud <daniel@firewall-services.com> - 0.1.1-1.sme
- Fix closing parenthesis on prop method in httpd template

* Wed Jul 26 2017 Daniel Berteaud <daniel@firewall-services.com> - 0.1.0-1.sme
- Initial release

 Sun Jun 26 2016 Jean-Philipe Pialasse <tests@pialasse.com> 2.6.0-4.sme
- clean daily session and tmp folders [SME: 9626]
- updated path for ibays' session and tmp folders to /var/cache

* Thu Jun 23 2016 Jean-Philipe Pialasse <tests@pialasse.com> 2.6.0-3.sme
- add tmp folder to ibays [SME: 7011]
- add session folder to ibays [SME: 9620]
- change global session folder from /tmp to /var/lib/php/session/ [SME: 139]

* Thu Mar 31 2016 Jean-Philipe Pialasse <tests@pialasse.com> 2.6.0-2.sme
- remove deprecated  allow_call_time_pass_reference from php.ini [SME: 9416]

* Fri Feb 05 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 2.6.0-1.sme
- Initial release to sme10

* Mon Jun 29 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 2.4.0-5
- revert the e-smith-php-2.4.0_add_upload_tmp_folder.patch [SME: 7011]

* Fri Nov 14 2014 Charlie Brady <charlie_brady@mitel.com> 2.4.0-4.sme
- Remove obsolete gpc_order setting from php.ini. [SME: 8652]

* Sun May 4 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 2.4.0-3.sme
- Add an upload_tmp_folder setting by db command [SME: 7011]
- Thanks to Michael McCarn and Jean-philippe Pialasse

* Sun May 19 2013 Ian Wells <esmith@wellsi.com> 2.4.0-2.sme
- Force magic_quotes Off [SME: 7605]

* Wed Feb 13 2013 Shad L. Lords <slords@mail.com> 2.4.0-1.sme
- Roll new stream for sme9

* Mon Sep 19 2011 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-6.sme
- Remove PHP version check from migrate script [SME: 6727]

* Mon Sep 19 2011 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-5.sme
- Obsolete magic_quotes settings [SME: 6725]

* Sat Sep 17 2011 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-4.sme
- Set default timezone [SME: 6716]

* Mon Jul 19 2010 Ian Wells <esmith@wellsi.com> 2.2.0-3.sme
- Default expose_php in php.ini to Off [SME: 6136]

* Sun Mar 14 2010 Jonathan Martens <smeserver-contribs@snetram.nl> 2.2.0-2.sme
- Prepare for obsoletion of magic_quotes* when we supply PHP 5.3.0+ [SME: 5843]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Wed Aug 20 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.12.0-8
- Fix latest patches to prevent .orig file [SME: 4513]

* Wed Aug 20 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.12.0-7
- Fix some minor layout issues introduced by fixes in [SME: 4513]

* Tue Aug 19 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.12.0-6
- Fix whiteline and spacing issues [SME: 4513]

* Fri Apr 18 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.12.0-5
- Split 80ModuleSettings template fragmenent to have one frament per module [SME: 3282]

* Fri May 18 2007 Shad L. Lords <slords@mail.com> 1.12.0-4
- Use correct lib for modules

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Fri Oct 13 2006 Shad L. Lords <slords@mail.com> 1.12.0-02
- Add support for php5 [SME: 1120]

* Fri Mar 17 2006 Gordon Rowell <gordonr@gormand.com.au> 1.12.0-01
- Roll stable stream version. [SME: 1016]

* Mon Jan 30 2006 Charlie Brady <charlie_brady@mitel.com> 1.11.0-10
- Remove all pre/post/preun/postun scriptlets. [SME: 469]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.11.0-09
- Bump release number only

* Tue Oct 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-08]
- Prevent i-bay name aliasing in default open_basedir restriction.
  [SF: 1330228]

* Tue Sep  6 2005 Tony Clayton <apc@e-smith.com>
- [1.11.0-07]
- Turn register_globals off by default [SF: 1271218]

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-06]
- Update to current db access APIs, in readiness for move of dbs to private
  directory. [SF: 1216546 (Shad)]

* Sun May  1 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-05]
- Update include_path in php.ini, to base and add-on pear directories.

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-04]
- Use generic_template_expand action to expand /etc/php.ini.
  Add e-smith-lib dependency. Add e-smith-devtools dependency. [MN00064130]
- Remove anachronisms in /etc/php.ini templates.
- Fix loss of AllowUrlFopen property during post-install. [MN00064752]

* Wed Nov 10 2004 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-03]
- Convert apache config fragments to apache2 format. [charlieb MN00051144]

* Fri Nov  5 2004 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-02]
- Remove specification of dynamic extensions, as that is done with newer
  php via /etc/php.d/.  [charlieb MN00051515]
- Replace deprecated Copyright header with License header.
- Remove bogus WARNING text from spec file. [charlieb]

* Mon Jan 26 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-01]
- rolling to dev - 1.11.0

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Changing version to stable stream number - 1.10.0

* Wed May 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-13]
- Fixed a typo in the previous version. [msoulier 8852]

* Wed May 28 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-12]
- Wrappered the restart of the e-smith web server so that it is conditional on
  e-smith-apache being installed. [msoulier 8852]

* Tue May 27 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-11]
- Remembered that we can't query the rpm database during rpm installs.
  [msoulier 8852]

* Tue May 27 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-10]
- Wrappered the restart of the e-smith web server so that it is conditional on
  e-smith-apache being installed. [msoulier 8852]

* Tue May 27 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-09]
- Added a type default fragment. [msoulier 3299]

* Wed Apr 23 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-08]
- Increase limits to allow webmail attachments of 10MB, rather than 2MB
  MemoryLimit 8M -> 32M, PostMaxSize 8M -> 20M, UploadMaxFilesize 2M -> 10M [gordonr 8478]

* Wed Apr  2 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-07]
- set allow_url_fopen = Off by default, tunable in config db [gordonr 4970]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-06]
- And back out last change - not a bug [gordonr 7836]

* Tue Apr  1 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-05]
- Fix include_path in php.ini [gordonr 7836]

* Fri Mar  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-04]
- Update more httpd.conf fragments to new interface [gordonr 7600]

* Fri Mar  7 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.9.0-03]
- Update httpd.conf fragment to new interface [gordonr 7600]

* Thu Jan 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-02]
- Adding .phtml extension. [msoulier 6543]

* Thu Jan 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.9.0-01]
- rolling to development stream to 1.9.0

* Thu Jan 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.8.0-05]
- Backing out changes since 1.8.0-01, as they belong in a development stream.
  [msoulier 6543]

* Thu Jan 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.8.0-04]
- Fixed a syntax error that I should have caught before committing the last
  version. [msoulier 6543]

* Thu Jan 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.8.0-03]
- Bringing the api up to the modern version. [msoulier 6543]

* Thu Jan 23 2003 Michael Soulier <msoulier@e-smith.com>
- [1.8.0-02]
- Added index.phtml to the DirectoryIndex directive, and made the code a
  little nicer to look at. [msoulier 6543]

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Roll to maintained version number to 1.8.0

* Mon Jul 22 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-01]
- Add conf-php link to bootstrap-console-save event [charlieb 1939]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-01]
- Changing version to development stream number to 1.7.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [1.6.0-01]
- Changing version to maintained stream number to 1.6.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.5-01]
- RPM rebuild forced by cvsroot2rpm

* Fri Mar 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.4-01]
- Turned off display_errors, use error_log -> syslog instead, as per
  Dan Brown's PHP upgrade HOWTO
- Tidied up formatting in that fragment [gordonr 3019]

* Fri Mar 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.3-01]
- Imported into CVS

* Fri Mar 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [1.5.1-01]
- rollRPM: Rolled version number to 1.5.1-01. Includes patches up to 1.5.0-03.

* Mon Feb 04 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-03]
- Remove all comments from php.ini template fragments.
- Allow some resource limits to be set by properties of the php service
  in the config db.

* Mon Feb 04 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-02]
- Template /etc/php.ini, and expand template during conf-php action.
- Make some simplifications to the conf-php script, and remove a
  potential error case (php is not in config db and event is neither
  post-install or post-upgrade).

* Mon Feb 4 2002 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-01]
- rollRPM: Rolled version number to 1.5.0-01. Includes patches up to 1.4.0-03.

* Thu Sep 6 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-03]
- Restrict PHP programs residing in an i-bay to only be able to open files
  which reside in the same i-bay. An i-bay property PHPBaseDir is available
  to override this restriction.

* Fri Aug 17 2001 gordonr
- [1.4.0-02]
- Autorebuild by rebuildRPM

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-02.

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-02]
- Load PHP modules late, not first. This corrects a compatibility problem
  with RedHat 7.1 RPMS.

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-01]
- Rolled version number to 1.3.0-01. Includes patches upto 1.2.0-05.

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-05]
- Changed license to GPL

* Fri Mar 23 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-04]
- Disable PHP MIME type by default
- Enable PHP MIME type for each i-bay for which dynamic content is enabled.

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-03]
- Rolling release number for GPG signing.

* Thu Jan 25 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-02]
- changed action to run at 50, instead of 55.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-10.

* Wed Jan 17 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-10]
- PHP is enabled by default.

* Fri Jan 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-9]
- rolling to 9, 8 is missing.
- pulling expand httpd.conf, we'll leave conf-httpd
  to do it.

* Thu Jan 11 2001 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-8]
- pulled restarting apache - just expand httpd.conf

* Thu Jan 11 2001 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-7]
- apache now restarts whenever php's status changes

* Thu Jan 11 2001 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-6]
- expand httpd.conf template from conf-php

* Thu Jan 11 2001 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-5]
- add apache restart code to conf-php

* Sat Jan  6 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-4]
- Only run %post actions in runlevel 7

* Fri Jan  5 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-3]
- put createlinks back in.

* Fri Jan  5 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-2]
- expand PHP httpd.conf fragments conditionally based on
  service status.
- add PHP to the services database and default to disabled.

* Wed Dec 06 2000 Peter Samuel <peters@e-smith.com>
- [1.1.0-1]
- Rolled version to 1.1.0-1. Inlcudes patches up to 0.1-1.

* Tue Nov 14 2000 Adrian Chung <adrianc@e-smith.com>
- initial release
