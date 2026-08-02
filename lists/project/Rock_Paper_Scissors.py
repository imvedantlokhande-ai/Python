import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image = [rock , paper , scissors]
choice = int(input("what do you choose? Type 0 for 'rock' 1 for 'paper' 2 for 'scissors'\n"))
print("your choice")
if choice >= 0 and choice < len(game_image)-1:
    print(game_image[choice])
computer_choice= random.randint(0,2)
print("Computer chose:")
print(game_image[computer_choice])

if choice>= 3 or choice< 0:
    print("you typed an invalid option")
elif choice==0 and computer_choice==2 :
    print("You win")
elif choice==2 and computer_choice==0 :
    print("You lose")
elif choice < computer_choice :
    print("You win")
elif choice > computer_choice :
    print("You lose")
elif choice == computer_choice :
    print("It's a tie")