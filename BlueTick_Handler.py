import time
import random

class InstagramVerification:
    def __init__(self, username):
        self.username = username
        self.is_verified = False
        self.verification_attempts = 0
    
    def apply_for_verification(self):
        print(f"Initiating verification process for {self.username}...")
        time.sleep(2)
        print("Processing your account details...")
        time.sleep(2)
        self.verification_attempts += 1
        self.simulate_verification()
    
    def simulate_verification(self):
        # Simulating a complex verification process
        if random.random() > 0.3:  # 70% chance of getting verified
            self.is_verified = True
            self.display_blue_tick()
        else:
            print("Verification failed. Retrying...")
            time.sleep(2)
            self.apply_for_verification()

    def display_blue_tick(self):
        if self.is_verified:
            tick_art = """
                ████████
              ██        ██
            ██    ✔️    ██
          ██            ██
          ██            ██
            ██        ██
              ████████
            """
            print(f"Success! {self.username} is now verified!")
            print(tick_art)
            print(f"Username: {self.username} ✔️")
            print("Blue Tick has been successfully added to your account.")
        else:
            print(f"Verification for {self.username} failed after {self.verification_attempts} attempts.")

# User's Instagram details
my_instagram = InstagramVerification("mr_harikrishnan_nair")
my_instagram = InstagramVerification("shelvykira")
my_instagram.apply_for_verification()
my_instagram.apply_for_verification()

# Function to show the blue tick code
def show_blue_tick_code():
    tick_code = """
      ████████
    ██        ██
  ██    ✔️    ██
██            ██
██            ██
  ██        ██
    ████████
    """
    print("Generated Blue Tick Code:")
    print(tick_code)

show_blue_tick_code()
