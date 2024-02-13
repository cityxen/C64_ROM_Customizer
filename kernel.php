<?php

$d=getcwd();
$filesize = filesize("$d\kernel.rom");
$fp = fopen("$d\kernel.rom", 'rb');
$binary = fread($fp, $filesize);
fclose($fp);

for($i=0;$i<37;$i++) $line1a[$i]=$binary[$i+1141];
for($i=0;$i<17;$i++) $line2a[$i]=$binary[$i+1178];

$line1=implode("",$line1a);
$line2=implode("",$line2a);

$border = bin2hex($binary[3289]);
$bkg    = bin2hex($binary[3290]);
$txt    = bin2hex($binary[1333]);

echo "line1 : $line1\n\r";
echo "line2 : $line2\n\r";
echo "border: \$$border\n\r";
echo "bkg   : \$$bkg\n\r";
echo "txt   : \$$txt\n\r";
