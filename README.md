# Random-Testing-Hands-On

Description of Random-Testing-Hands-On:   
Depending on the credit card issuer, the length of a credit card number can range between 10 and 19 digits. The first few digits of the number are the issuer prefix. Each credit card issuer has an assigned range of numbers. For example, only Visa credit card numbers may begin with 4, while American Express card numbers must begin with either a 34 or 37. Sometimes, credit card providers are assigned multiple ranges. For example, MasterCard card numbers must start with the numbers between 51 through 55 or 2221 through 2720 (inclusive). 

The last digit of the number is referred to as the check digit and acts as a checksum. Most credit cards calculate this check digit using the Luhn algorithm (see resources below for how this is calculated).

In order to limit the scope of this assignment, we are going to limit the number of credit card issuers to 3: Visa, MasterCard, and American Express. Each has their own prefixes and length requirements.

-Visa:
  * Prefix(es): 4    
  * Length: 16  
-MasterCard:
  * Prefix(es): 51 through 55 and 2221 through 2720     
  * Length: 16                 
-American Express:
  * Prefix(es): 34 and 37                  
  * Length: 15                
  
  
  Work Citation:
  https://replit.com/@coeCS362/random1:         
     * for i in range(0,1000):
           val = random.randint(10000000,99999999)
           mystery_func(val)
