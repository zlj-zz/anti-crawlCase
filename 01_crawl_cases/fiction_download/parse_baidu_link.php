<?php

//$url = "http://www.baidu.com/link?url=-LUKEQwP_-G-_k-gSzu5NM7vKzz3of3PXV_F8w1-HjZbagIXXCC2dSY1RHYgmCQd";
$url = $argv[1];


$info = parse_url($url);
$fp = fsockopen($info['host'], 80,$errno, $errstr, 30);
fputs($fp,"GET {$info['path']}?{$info['query']} HTTP/1.1\r\n");
fputs($fp, "Host: {$info['host']}\r\n");
fputs($fp, "Connection: close\r\n\r\n");
$rewrite = '';
while(!feof($fp)) {
    $line = fgets($fp);
    if($line != "\r\n" ) {
        if(strpos($line,'Location:') !== false) {
            $rewrite = str_replace(array("\r","\n","Location: "),'',$line);
        }
    }else {
        break;
    }
}
var_dump($rewrite); //结果显示：string(22) "http://www.google.com/" 
?>
