def main():
    with open('testing text.txt','r',encoding='utf-8') as file:
        score = 0
        score2 = 0
        for line in file:
            score += calculate_points(line.strip())
            score2 += calculate_points2(line.strip())
        print(score,score2)

def calculate_points(choices:str) -> int:
    WIN = 6
    DRAW = 3
    LOSS = 0

    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    game_scores = {
    'A X': DRAW + ROCK,
    'A Y': WIN + PAPER,
    'A Z': LOSS + SCISSORS,
    'B X': LOSS + ROCK,
    'B Y': DRAW + PAPER,
    'B Z': WIN + SCISSORS,
    'C X': WIN + ROCK,
    'C Y': LOSS + PAPER,
    'C Z': DRAW + SCISSORS,
}
    return game_scores[choices]

def calculate_points2(choices:str) -> int:
    WIN = 6
    DRAW = 3
    LOSS = 0

    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    # A = ROCK
    # B = PAPER
    # C = SCISSORS

    game_scores = {
    'A X': LOSS + SCISSORS,
    'A Y': DRAW + ROCK,
    'A Z': WIN + PAPER,
    'B X': LOSS + ROCK,
    'B Y': DRAW + PAPER,
    'B Z': WIN + SCISSORS,
    'C X': LOSS + PAPER,
    'C Y': DRAW + SCISSORS,
    'C Z': WIN + ROCK,
}
    return game_scores[choices]

if __name__ == '__main__':
    main()
