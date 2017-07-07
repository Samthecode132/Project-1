
print("After a long hard day at work, you find yourself collapsed on your bed. You succumb to a deep sleep and that's when your adventure begins.")

answer=input("Would You Like To Be A Princess or A Peasant? Type 'Princess' or 'Peasant':")
if answer=="Princess":
    print("You Are Located In Your Kingdom. You Have Just Reached Two Gold Encrusted Roads Diverging." )
    user_input=input("Would you like to turn left or right? Type 'Left' or 'Right':")
    if user_input == "Left":
        print("You Choose To Go Left. You Have Just Come Across A Wizard.")
        question=input("Choose: Fight or Run")
        if question == "Fight":
            print("You Choose to Fight. The Wizard Transforms You Into A Frog! Game Over.")

        else:
            print("You Choose To Run And You Escape Safely! Game Over.")



    elif user_input == "Right":
        print("You Have Just Come Across A Fire Breathing Dragon!")
        sam=input("Choose:'Tame' the Dragon or 'Kill' the Dragon:")
        if sam == "Tame":
            print("You Choose to Tame the Dragon. You Were Successful And Now You Have A New Pet! Game Over.")

        else:
            print("You Choose To Kill The Dragon And Got A Delicious Meal! Game Over.")

    else:
       print("That Is Not A Valid Answer.")

if answer == "Peasant":
    print("You Are Located In The Middle Of A Dark Forest. You Have Just Reached Two Dirt Roads Diverging.")
    user_input=input("Would you like to turn left or right? Type 'Left' or 'Right':")
    if user_input == "Left":
         print("You Choose To Go Left. You Have Come Across A River.")
         question=input("Choose:'Cross the River' or 'Stay Put':")
         if question == "Cross the River":
             print("You Choose to Cross the River. However, the Current is Too Strong And You Drown! Game Over.")

         else:
             print("You Choose To Stay Put And You Take a Nap! Game Over.")




    elif user_input == "Right":
         print("You Have Disturbed The Sleep Of a Samurai!")
         kat=input("Choose:'Fight' or 'Run':")
         if kat == "Fight":
             print("You Choose to Fight the Samurai. However, the Samurai Defeats You in a Fatal Blow! Game Over.")

         else:
             print("You Choose To Run Away! However, You Trip Over A Pebble And Die! Game Over.")


    else:
       print("That Is Not A Valid Answer.")
