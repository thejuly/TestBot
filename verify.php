<?php
$access_token = '1sAimDh9L0wg5XAJeBYy96GrwzZFYQYAfTB+CrsdX5E/9gdt9oj5Lbc9NbRSHh5d05Ne9FDan12z6c9dbprv5TXRgjm4/+ioHTy6G91A2rNBiW999c0IlhsTcq5bfOyVf7OLRGtAAISIbHd84WemFgdB04t89/1O/w1cDnyilFU= ';

$url = 'https://api.line.me/v1/oauth/verify';

$headers = array('Authorization: Bearer ' . $access_token);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
$result = curl_exec($ch);
curl_close($ch);

echo $result;