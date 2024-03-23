<?php
if (isset($_SERVER['REDIRECT_REMOTE_USER'])) {
   $_SERVER['REMOTE_USER']= $_SERVER['REDIRECT_REMOTE_USER'];
}
if (isset($_SERVER['REDIRECT_HTTP_AUTHORIZATION'])) {
   $_SERVER['HTTP_AUTHORIZATION']=$_SERVER['REDIRECT_HTTP_AUTHORIZATION'];
   $hash = str_replace('Basic ', '', $_SERVER['HTTP_AUTHORIZATION']);
   $hash = base64_decode($hash);error_log($hash);
   if (strpos($hash, ':') !== false) {
      list( $_SERVER['PHP_AUTH_USER'], $_SERVER['PHP_AUTH_PW']) = explode(':', $hash, 2);
   }
}

if (isset($_SERVER['HTTP_AUTH_TKT'])) {
   $hash = base64_decode($_SERVER['HTTP_AUTH_TKT']);
   if (strpos($hash, '!') !== false) {
      list ( $auth, $timehost) = explode('!', $hash, 2);
      $_SERVER['TOKEN'] = substr($auth,0,72);
      $_SERVER['PHP_AUTH_USER']=  $_SERVER['REMOTE_USER'];
   }
}
?>
