import threading
from playsound import playsound

def play_music(file_path):
    playsound(file_path)

def game_logic():
    print("Starting game...")

    print("Вітаю в грі 'Кольорові загадки та вікторини'!")

    score = 0

    a = input("Якого кольору жук оленнь: чорного, червоного, зеленого, кремового? ")
    if a == 'чорного':
        print('Відповідь не правильна. Це був загадковий чорний жук!')
    elif a == 'червоного':
        print('Відповідь не підходить, але цей колір виглядає гармонійно. Спробуйте ще!')
    elif a == 'зеленого':
        print('Відповідь не правильна. Можливо, цей жук змінить свій колір вам в очі!')
    elif a == 'кремового':
        print('Відповідь правильна! Цей жук дійсно кремовий.')
        score += 1

        # Question 2
    a = input("\nСкільки букв в китайських ієрогліфах: 1, 100, 1000, 47,035? ")
    if a == '1':
        print('Відповідь не правильна. Китайські ієрогліфи багато, але це лише початок.')
    elif a == '100':
        print('Відповідь не правильна. Спробуйте ще, кількість більша!')
    elif a == '1000':
        print('Відповідь не правильна. Китайська мова вражає своєю складністю.')
    elif a == '47 035':
        print('Відповідь правильна! Дійсно, багато букв у китайських ієрогліфах.')
        score += 1

    a = input("\nСкільки буде гіперзарядів у грі Brawl Stars в новому сезоні: 1, 5, 4, 2? ")
    if a == '1':
        print('Відповідь не правильна. Бравл стар змінюється!')
    elif a == '5':
        print('Відповідь не правильна. Спробуйте ще, кількість менша.')
    elif a == '4':
        print('Відповідь не правильна. Пошукайте оновлення!')
    elif a == '2':
        print('Відповідь правильна! У вас добре оновленої гри Brawl Stars.')
        score += 1

    a = input("\nЯк називається столиця Японії? ")
    if a.lower() == 'токіо':
        print('Відповідь правильна! Токіо - столиця Японії.')
        score += 1
    else:
        print('Відповідь не правильна. Спробуйте ще!')

    print("\nДякую за гру в 'Кольорові загадки та вікторини'!")
    print("Ваш результат:", score, " з 4")

    print("Game over.")

# Specify the path to your music file
music_file_path = "lev.mp3"

# Create a thread for playing music
music_thread = threading.Thread(target=play_music, args=(music_file_path,))

# Start the music thread
music_thread.start()

# Your main game logic
game_logic()

# Wait for the music thread to finish
music_thread.join()
