#OTP
actual_otp = 5678
attempts = 3

# otp_count = str(otp)
# otp_count = len(otp_count)
# print(otp_count)
while attempts:
    otp = int(input("Enter 4 digit OTP "))
    if len(str(otp)) != 4:
        print("OTP must be 4 digits")
    if otp == actual_otp:
        print("OTP is correct ")
        break
    attempts = attempts - 1
else:
    print("maxium attempts reached")


