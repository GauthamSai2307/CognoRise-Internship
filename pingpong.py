import random

def user_hit():
    input("Press Enter to hit the ball.")

def ai_hit():
    print("AI is hitting the ball...")

def user_serve():
    input("Press Enter to serve.")

def ai_serve():
    print("AI is serving...")

def user_wins_point():
    print("User wins the point!")

def ai_wins_point():
    print("AI wins the point!")

def draw():
    print("It's a draw!")

def play_ping_pong():
    user_score = 0
    ai_score = 0

    while True:
        user_serve()
        ai_hit()
        if random.choice([True, False]):
            user_wins_point()
            user_score += 1
        else:
            ai_wins_point()
            ai_score += 1

        print("Score: User -", user_score, ", AI -", ai_score)

        if user_score >= 21 and user_score - ai_score >= 2:
            print("User wins the match!")
            break
        elif ai_score >= 21 and ai_score - user_score >= 2:
            print("AI wins the match!")
            break

        ai_serve()
        user_hit()
        if random.choice([True, False]):
            ai_wins_point()
            ai_score += 1
        else:
            user_wins_point()
            user_score += 1

        print("Score: User -", user_score, ", AI -", ai_score)

        if user_score >= 21 and user_score - ai_score >= 2:
            print("User wins the match!")
            break
        elif ai_score >= 21 and ai_score - user_score >= 2:
            print("AI wins the match!")
            break

        if user_score == 20 and ai_score == 20:
            print("Deuce! Continuing...")
            continue

play_ping_pong()
