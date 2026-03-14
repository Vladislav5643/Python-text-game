import time

# --- INITIALIZATION ---
print("Welcome To The Shadow in Museum")
print("Warning: Game has strong language and violence")
print("Write your name: ")
name = input(">> ")

print(f'Accepted. Now you are - {name}, Guard of the Museum')
time.sleep(1)
print("\nTime - 23:45. The lights disappear everywhere. The sound of breaking glass...")
print("In 10 seconds of total darkness, the Diamond 'Eye of the Sun' has vanished.")
time.sleep(1)
print("I am your interface. Every choice you make will shape your story.")
time.sleep(1)
print("\nThe doors are automatically locked. In the corridor, only two people remain near the broken glass.")
time.sleep(1)
print("1. Marcus: Breathing heavily. His flashlight is broken, his arms are trembling. He says someone pushed him.")
print("2. Eleonora: Quietly adjusts her dress. She seems unusually calm about the theft.")

# --- ACTION I ---
print("\nYour choice:")
print("1 - Ask Marcus what he saw and examine him")
print("2 - Check Eleonora's handbag")
print("3 - Examine the broken glass")
choice1 = input(">> ")

if choice1 == "1":
    print("\nYou approach Marcus. He looks scared to death. His hands are covered in a glowing magical powder.")
    print("Marcus: 'Inspector, I swear I heard a whisper. A spell in an old language. Then BOOM. Something cold pushed me.'")
    time.sleep(2)
    print("\nSystem: You realize this is an Unusual Robbery. The powder is a magical catalyst used for teleportation.")
    print("Marcus is innocent, but he touched the villain while they were invisible.")
    
    # --- ACTION II ---
    print("\nAction II: The Search in Shadows")
    time.sleep(1)
    print("Thanks to the glowing powder, you see a trail leading to the ventilation.")
    print("Suddenly, Eleonora screams: 'You're wasting time on this loser! I saw someone run to the North Exit!'")
    print("\nYour Choice:")
    print("1 - Follow the magical dust trail to the Old Chapel")
    print("2 - Intercept Eleonora. Her distraction is too suspicious")
    
    choice2 = input(">> ")

    if choice2 == "2":
        print("\nYou block Eleonora's path. She tries to push you away, but you grab her arm.")
        print("Under her silk glove, you find the SAME purple powder! She's a collaborator!")
        time.sleep(2)
        print("\nEleonora: 'You're too smart for a simple guard. This diamond is my family's heart!'")
        print("She smashes a smoke vial and runs toward the Secret Relics Hall.")
        time.sleep(2)

        # --- ACTION III ---
        print("\nAction III: The Final Confrontation")
        print("You burst into the hall. Eleonora is in a magic circle. The Diamond 'Eye of Sun' glows blood-red.")
        print("The portal is opening. You have only ONE chance to stop her!")
        time.sleep(1)
        
        print("\nYour Final Choice:")
        print("1 - Throw Marcus's broken flashlight into the circle (Electrical disruption)")
        print("2 - Use your camera's flash to blind her (Flash of Light)")
        print("3 - Try to reason with her (Words of Truth)")
        
        final_choice = input(">> ")

        if final_choice == "1":
            print("\nBOOM! The metal and sparks from the flashlight short-circuit the magic!")
            print("The portal collapses, knocking Eleonora unconscious. The diamond is safe.")
            print(f"\nCongratulations, {name}! You saved the Museum. CASE CLOSED.")
        elif final_choice == "2":
            print("\nFLASH! Eleonora is blinded for a second and drops the diamond.")
            print("The ritual breaks! You tackle her before she can reach the stone.")
            print(f"\nGreat job, {name}! The Eye of the Sun remains in the museum.")
        elif final_choice == "3":
            print("\nYou try to speak, but the portal is too loud. She doesn't listen.")
            print("Eleonora steps into the light and vanishes with the diamond forever.")
            print(f"\nGAME OVER. You failed, {name}. The shadows took the prize.")
        else:
            print("\nYou hesitated too long. The portal consumed everything.")
            print("GAME OVER.")

    else:
        # Choice 2 == "1"
        print("\nYou followed the dust to the Chapel, but it was a decoy trail.")
        print("By the time you realized it, Eleonora had already escaped through the roof.")
        print(f"GAME OVER. Better luck next time, {name}.")

elif choice1 == "2":
    print("\nYou try to grab Eleonora's bag. She screams 'Harassment!' and the museum's automated security dazes YOU instead.")
    print("By the time you wake up, everyone is gone. GAME OVER.")

elif choice1 == "3":
    print("\nYou look at the glass. It broke OUTWARDS. The thief was inside the case?")
    print("While you're analyzing physics, someone hits you on the back of the head.")
    print("Everything goes dark. GAME OVER.")

else:
    print("\nInvalid choice. The thief escaped while you were standing still!")