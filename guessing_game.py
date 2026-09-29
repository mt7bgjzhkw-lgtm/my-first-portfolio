import random


def guessing_game():
    print("--- مرحباً بكِ في لعبة تخمين الأرقام الذكية! ---")
    print("اخترت رقماً عشوائياً بين 1 و 100. هل يمكنك تخمينه؟\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            user_guess = int(input("ادخلي تخمينك (رقم بين 1 و 100): "))
            attempts += 1

            if user_guess < secret_number:
                print("رقم صغير جداً! جربي تدورين على رقم أكبر 📈.")
            elif user_guess > secret_number:
                print("رقم كبير جداً! جربي تدورين على رقم أصغر 📉.")
            else:
                print(f"\n🎉 كفو! لقد فزتِ! الرقم الصحيح هو {secret_number}.")
                print(f"استغرقتِ {attempts} محاولات فقط لإيجاده.")
                break
        except ValueError:
            print("خطأ: الرجاء إدخال رقم صحيح فقط!")


if __name__ == "__main__":
    guessing_game()