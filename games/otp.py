import math, random
def generateOTP() :
    digits = "0123456789"
    OTP = ""
    n = int(input("enter no. 4 or 6 :- "))
    for i in range(n) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP
 
if __name__ == "__main__" :
     
    print("OTP:", generateOTP())
