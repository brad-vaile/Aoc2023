import time

entries = []
games = []

max_red_cubes = 12
max_green_cubes = 13
max_blue_cubes = 14


def split_input(input : str):
    split_string = input.split(":")
    split_string[1] = split_string[1].strip()
    games.append(split_string)

def check_game_possible(game_cubes):
    game_turns = game_cubes.split(";");
    for turn in game_turns:
        cubes_shown = turn.split(',');
        for c in cubes_shown:
            cube_amount = int(c.strip().split(' ')[0])
            if(c.find('green') != -1):
                if(cube_amount > max_green_cubes):
                    return False
            if(c.find('red') != -1):
                if(cube_amount > max_red_cubes):
                    return False;
            if(c.find('blue') != -1):
                if(cube_amount > max_blue_cubes):
                    return False;
    return True;

def load_file():
    with open(r'') as input_file:
        for line in input_file:
            entries.append(line.replace("\n", ""))

if __name__ == '__main__':
    start = time.time()
    load_file()
    inputNumbers = []
    for entry in entries:
        split_input(entry);
    
    valid_games = []
    for game in games:
        if(check_game_possible(game[1])):
            valid_games.append(int(game[0].split(" ")[1]))

    print(valid_games);
    print(sum(valid_games))

    end = time.time()
    print(f"Time taken to run the code was {end - start} seconds")


