Rem Delete download files
del c:\AsiaMile\Shell\Report\Decrypt\*.* /Q
del c:\AsiaMile\Shell\Report\*.* /Q


"C:\Program Files (x86)\WinSCP\WinSCP.exe" /ini=nul /script=c:\AsiaMile\Shell\Script\MFT_Report.txt
Rem wait 2 seconds
echo %time%
timeout 2 > NUL
echo %time%
Rem Copy files to decrypt folder for decryption
xcopy c:\AsiaMile\Shell\Report\*.* c:\AsiaMile\Shell\Report\Decrypt\*.* /Y 

Rem decrypt dedicated files
cd c:\AsiaMile\Shell\Report\Decrypt\

Rem decrypt dedicated files
gpg --batch --passphrase Robin2016? --keyring "c:\AsiaMile\key\elegant-AM-prod_key.asc"  -o "c:\AsiaMile\Shell\Report\Decrypt\sz4.rpt" -d "c:\AsiaMile\Shell\Report\Decrypt\sz4.rpt.asc" 
gpg --batch --passphrase Robin2016? --keyring "c:\AsiaMile\key\elegant-AM-prod_key.asc"  -o "c:\AsiaMile\Shell\Report\Decrypt\sz4.mis" -d "c:\AsiaMile\Shell\Report\Decrypt\sz4.mis.asc" 
gpg --batch --passphrase Robin2016? --keyring "c:\AsiaMile\key\elegant-AM-prod_key.asc"  -o "c:\AsiaMile\Shell\Report\Decrypt\sz4.hb" -d "c:\AsiaMile\Shell\Report\Decrypt\sz4.hb.asc" 


Rem Copy files to sFTP folder for sending emails
copy c:\AsiaMile\Shell\Report\Decrypt\sz4.rpt C:\sFTPRoot\Report\AsiaMiles\sz4-%date:~10,4%%date:~4,2%%date:~7,2%.rpt
copy c:\AsiaMile\Shell\Report\Decrypt\sz4.hb C:\sFTPRoot\Report\AsiaMiles\sz4-%date:~10,4%%date:~4,2%%date:~7,2%.hb
copy c:\AsiaMile\Shell\Report\Decrypt\sz4.mis C:\sFTPRoot\Report\AsiaMiles\sz4-%date:~10,4%%date:~4,2%%date:~7,2%.mis 

Rem Copy files to wwwroot
copy c:\AsiaMile\Shell\Report\Decrypt\sz4.rpt C:\inetpub\wwwroot\AM1\Report\sz4-%date:~10,4%%date:~4,2%%date:~7,2%.rpt
copy c:\AsiaMile\Shell\Report\Decrypt\sz4.hb C:\inetpub\wwwroot\AM1\Report\sz4-%date:~10,4%%date:~4,2%%date:~7,2%.hb
copy c:\AsiaMile\Shell\Report\Decrypt\sz4.mis C:\inetpub\wwwroot\AM1\Report\sz4-%date:~10,4%%date:~4,2%%date:~7,2%.mis 

REM rename reports
ren c:\AsiaMile\Shell\Report\Decrypt\sz4.rpt c:\AsiaMile\Shell\Report\Decrypt\sz4-%date:~10,4%%date:~4,2%%date:~7,2%.rpt
ren c:\AsiaMile\Shell\Report\Decrypt\sz4.hb c:\AsiaMile\Shell\Report\Decrypt\sz4-%date:~10,4%%date:~4,2%%date:~7,2%.hb
ren c:\AsiaMile\Shell\Report\Decrypt\sz4.mis c:\AsiaMile\Shell\Report\Decrypt\sz4-%date:~10,4%%date:~4,2%%date:~7,2%.mis


del c:\AsiaMile\Shell\Report\Decrypt\*.asc /F /Q

python C:\AsiaMile\bin\putFileToGDrive.py


