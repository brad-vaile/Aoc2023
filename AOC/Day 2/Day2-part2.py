import time

entries = []
games = []

def split_input(input : str):
    split_string = input.split(":")
    split_string[1] = split_string[1].strip()
    games.append(split_string)

def get_minimum_cubes_value(game_cubes):
    required_red_cubes = 0;
    required_green_cubes = 0;
    required_blue_cubes = 0;

    game_turns = game_cubes.split(";");
    for turn in game_turns:
        cubes_shown = turn.split(',');
        for c in cubes_shown:
            cube_amount = int(c.strip().split(' ')[0])
            if(c.find('green') != -1):
                if(cube_amount > required_green_cubes):
                    required_green_cubes = cube_amount;
            if(c.find('red') != -1):
                if(cube_amount > required_red_cubes):
                    required_red_cubes = cube_amount;
            if(c.find('blue') != -1):
                if(cube_amount > required_blue_cubes):
                    required_blue_cubes = cube_amount;
    print('blue:')
    print(required_blue_cubes)
    return required_red_cubes * required_green_cubes * required_blue_cubes;

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
    
    total_value = 0
    for game in games:
        total_value += get_minimum_cubes_value(game[1])

    print(total_value)

    end = time.time()
    print(f"Time taken to run the code was {end - start} seconds")


