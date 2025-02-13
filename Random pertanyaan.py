import random

# Daftar pertanyaan dan jawaban
questions = {
    "Apa nama ilmu yang mempelajari tentang tumbuhan?": "Botani",
    "Apa nama ilmu yang mempelajari tentang hewan?": "Zoologi",
    "Apa nama ilmu yang mempelajari tentang mikroorganisme?": "Mikrobiologi",
    "Apa nama ilmu yang mempelajari tentang sel?": "Sitologi",
    "Apa nama ilmu yang mempelajari tentang fungsi tubuh manusia?": "Fisiologi",
}

def play_game():
    # Mengambil pertanyaan secara acak
    question, answer = random.choice(list(questions.items()))

    # Menampilkan pertanyaan kepada pemain
    print(f"\n{question}")

    # Menerima jawaban dari pemain
    user_answer = input("Jawaban Anda: ")

    # Memeriksa jawaban pemain
    if user_answer.lower() == answer.lower():
        print("Jawaban Anda benar!")
    else:
        print("Jawaban Anda salah. Jawaban yang benar adalah:", answer)

def main():
    print("Selamat datang di Game Tebak-tebakan Biologi!")
    print("Anda akan diberikan pertanyaan tentang biologi. Cobalah untuk menjawab dengan benar.")
    print("Jika Anda siap, mari kita mulai!")

    while True:
        play_game()

        # Menanyakan apakah pemain ingin bermain lagi
        play_again = input("Apakah Anda ingin bermain lagi? (ya/tidak): ")
        if play_again.lower() != "ya" and play_again.lower() !=  "y":
            print("Terima kasih telah bermain!")
            break

if __name__ == "__main__":
    main()
