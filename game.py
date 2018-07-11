import time 
import random
 
win = "You Win"
lose = "The Computer Wins"
lives = 5 
score = 0 
drew = 0 
computer_lives = 7 
password_list = []

while True : 
	username = input("Please , enter your username : ")
	password = input("Please , enter your password : ") 
	searchfile = open("accounts" ,"r" )
	for line in searchfile :
		password_list.append(line.strip())
		if password and username in password_list :  
			print("Access Granted ") 
			time.sleep(0.5)
			print("Loading . ")
			time.sleep(0.5)
			print("Loading . . ")
			time.sleep(0.5)
			print("Loading . . . ")
			time.sleep(0.5)
			print("====================================== ")
			print("Live Rules : ")
			print("You Start With : " , lives ," Lives ")
			print("If You Win You Will Get an Extra Live ")
			print("If You Lose You Will Lose a live ")
			print("If You Draw the lives stay the same ") 
			print("------------------------------------------ ")
			print("Make Sure You Don't Use CAPITALS ")
			print("------------------------------------------ ")
			print("Type [ display rules ] To see the list of rules ")	
			print("-------------------------------------------")
			print("Type [ display score ] to see your score")
			print("------------------------------------------ ")
			print("Type [ display drew  ] to display draws ")
			print("------------------------------------------")
			print("Type [ exit          ] to leave the game ")
			print("------------------------------------------")
			print("Type [ restart       ] to restart the game ")
			print("------------------------------------------")
			print("The Computer has lives aswell ")
			print("Can You beet the computer ? ")
			print("Good Lick !")
			print("------------------------------------------ ")
			while True : 
				rps = input("Rock , Paper , Scissors ? ") 
				computer = ("rock" , "paper" , "scissors")
				computer = random.choice(computer)
				# rock if statements 
				if rps == "rock" and computer == "paper" :
					print("computer choose : " , computer)
					print(" ")
					print(lose)
					print(" ")
					print(" ")
					lives -=1 
				if rps == "rock" and computer == "scissors" : 
					print("computer choose : " , computer)
					print(" ")
					print(win)
					print(" ")
					print(" ")
					score +=1 
				# paper statements 
				if rps == "paper" and computer == "rock" : 
					print("computer choose : " , computer)
					print(" ")
					print(win)
					print(" ")
					print(" ")
					score += 1 
				if rps == "paper" and computer == "scissors" : 
					print("computer choose : " , computer)
					print(" ")
					print(lose)
					print(" ")
					print(" ")
					lives -=1  
				# scissors statement 
				if rps == "scissors" and computer == "rock" : 
					print("computer choose : " , computer)
					print(" ")
					print(lose)
					print(" ")
					print(" ")
					lives -=1 


				if rps == "scissors" and computer == "paper" : 
					print("computer choose : " , computer)
					print(" ")
					print(win)
					print(" ")
					print(" ")
					score +=1 


				if rps == "rock" and computer == "rock" : 
					print("computer choose : " , computer)
					print(" ")
					print("You Drew")
					print(" ")
					print(" ")
					drew +=1 
				if rps == "paper" and computer == "paper" :  
					print("computer choose : " , computer)
					print(" ")
					print("You Drew")
					print(" ")
					print(" ")
					drew +=1 
				if rps == "scissors" and computer == "scissors" :  
					print("computer choose : " , computer)
					print(" ")
					print("You Drew")
					print(" ")
					print(" ")
					drew +=1 
				if rps == "display rules" : 
					print("**********************************")
					print("              rules               ")
					print("**********************************")
					print(" - Rock loses against Paper ")
					print(" - Rock beats Scissor ")
					print(" - Paper beats Rock ")
					print(" - Paper loses against Scissor ")
					print(" - Scissor beats Paper ")
					print(" - Scissor loses against Rock ")
					print("**********************************")

				if rps == "display lives" : 
					print(lives)

				if rps == "display score" : 
					print(score)
				if rps == "display drew" : 
					print(drew)


				if lives == 0 : 
					print("Thanks for Playing ")
					print("You have run out of lives ")
					print("You got " , score ," correct ")
					print("You drew " ,drew , " times ")
					stop = input("Press Enter to Exit : ") 
					
					time.sleep(900)
				if computer_lives == 0 : 
					print("Thanks for Playing ")
					print("Computer lost all its lives , You Win :) ")
					print("You got " , score ," correct ")
					print("You drew " ,drew , " times ")
					stop = input("Press Enter to Exit : ")
					time.sleep(900) 
				if rps == "exit" : 
					#break 
					exit()
				if rps == "restart" :
					break 
		else :
			print("your username or password is inncorrect , try again ... ")
			print("--------------------------------------------------------")

