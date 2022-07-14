Rem decrypt dedicated files
gpg --batch --passphrase Robin2016? --keyring "C:\AsiaMile\key\elegant-AM-prod_key.asc"  -o "c:\AsiaMile\Shell\Report\Decrypt\sz4.rpt" -d "c:\AsiaMile\Shell\Report\Decrypt\sz4.rpt.asc" 
gpg --batch --passphrase Robin2016? --keyring "C:\AsiaMile\key\elegant-AM-prod_key.asc"  -o "c:\AsiaMile\Shell\Report\Decrypt\sz4.mis" -d "c:\AsiaMile\Shell\Report\Decrypt\sz4.mis.asc" 
gpg --batch --passphrase Robin2016? --keyring "C:\AsiaMile\key\elegant-AM-prod_key.asc"  -o "c:\AsiaMile\Shell\Report\Decrypt\sz4.hb" -d "c:\AsiaMile\Shell\Report\Decrypt\sz4.hb.asc" 

pause
