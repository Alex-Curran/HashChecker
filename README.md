# HashChecker
Simple CLI Python application to check hash of a file. 
I wrote this program to help learn python. I am still learning so go easy :)! I plan on refactoring the code, and making it more readable. This is my first python program!

Use: 
  Enter path to file to be checked. (Complete path with file extension!)
  Enter expected hash
  Select hashing algorithm 
   - currently supports sha1, sha256, and md5. Uses hashlib, any algorithm supported by hashlib would be trivial to implement.
   I am using these 3 currently, until I refactor/cleanup the code. I plan on adding support for any algortihm listed in "hashlib.avialable_alogrithms" and only showing the user the algorthims they have avialable
   
 
 Speed is decent, further research is needed to see how I can improve it. I was able to compute a sha256 hash of the ubuntu installer in ~10 seconds.
 This is low priority atm...
