print("--------------------------------------")
print("Rock , Paper , Scissors Account Setup ")
print("--------------------------------------")
while True :  
	username = input("Enter a Username :  ")
	password = input("Enter a Password :  ")
	password_confirm = input("Please Confirm your Password :  ")
	if password_confirm != password : 
		print("your passwords don't match , please try again ... ")
	if password_confirm == password : 
		print("Your Account has been setup ")
		text_file = open("accounts",'a')
		text_file.write(username)
		text_file.write("\n")
		text_file.write(password)
		text_file.write("\n")
		text_file.close()
		break 
