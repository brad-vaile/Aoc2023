import time

## What on earth is this code - absolute hackathon

class gearRatio:
    def __init__(self, line, gearIndex, code):
        self.line = line
        self.gearIndex = gearIndex
        self.code = code

lines = []

def load_file():
    with open(r'') as input_file:
        for line in input_file:
            lines.append(line.replace("\n", ""))

def is_gear_char(character):
    return character == '*';

def get_full_number(line : str, index):
    forward_index = index+1;
    backward_index = index-1;
    start_of_line = False;
    end_of_line = False;
    full_number = '';
    full_number += line[index];
    while(not start_of_line and line[backward_index].isnumeric()):
        full_number = line[backward_index] + full_number
        backward_index -= 1;
        if(backward_index == -1):
            start_of_line = True;
    
    while(not end_of_line and line[forward_index].isnumeric()):
        full_number = full_number + line[forward_index];
        forward_index += 1;
        if(forward_index == len(line)):
            end_of_line = True;

    return int(full_number)


def get_engine_schematics():
    prev_line = None
    next_line = None

    gear_ratios = []
    for index, line in enumerate(lines):
        if(index != 0):
            prev_line = lines[index-1]
        
        if(index != len(lines)-1):
            next_line = lines[index+1]
  
        line_length = len(str(line))
        for cindex, character in enumerate(str(line)):
            engine_code = 0
            if(character.isnumeric()):
                if prev_line != None:
                    if(cindex > 0):
                        if(is_gear_char(prev_line[cindex-1])):
                            gear_ratios.append(gearRatio(index-1, cindex-1, get_full_number(line, cindex))); 
                    if(is_gear_char(prev_line[cindex])):
                         gear_ratios.append(gearRatio(index-1, cindex, get_full_number(line, cindex))); 
                    if(cindex < line_length-1):
                        if(is_gear_char(prev_line[cindex + 1])):
                           gear_ratios.append(gearRatio(index-1, cindex+1, get_full_number(line, cindex))); 
                if next_line != None:
                    if(cindex > 0):
                        if(is_gear_char(next_line[cindex-1])):
                           gear_ratios.append(gearRatio(index+1, cindex-1, get_full_number(line, cindex))); 
                    if(is_gear_char(next_line[cindex])):
                         gear_ratios.append(gearRatio(index+1, cindex, get_full_number(line, cindex))); 
                    if(cindex < line_length-1):
                        if(is_gear_char(next_line[cindex + 1])):
                           gear_ratios.append(gearRatio(index+1, cindex+1, get_full_number(line, cindex))); 
                
                if(cindex != line_length-1 and is_gear_char(line[cindex+1])):
                    gear_ratios.append(gearRatio(index, cindex+1, get_full_number(line, cindex))); 
                elif(cindex != 0 and is_gear_char(line[cindex-1])):
                    gear_ratios.append(gearRatio(index, cindex-1, get_full_number(line, cindex)));    

    gear_ratio_calculated = []
    for gear_ratio in gear_ratios:
        ## Ignore matching codes (should have removed duplicates earlier)
        # This only works because there is only ever 2 linked gear ratios 
        for matching_ratio in (x for x in gear_ratios if x.code != gear_ratio.code and x.line == gear_ratio.line and x.gearIndex == gear_ratio.gearIndex):
            gear_ratio_calculated.append(gear_ratio.code * matching_ratio.code)

    
    prev_code = 0
    final_codes = []
    for code in gear_ratio_calculated:
        if(code != prev_code):
            final_codes.append(code)
        prev_code = code
    print(sum(list(dict.fromkeys(final_codes))));

if __name__ == '__main__':
    start = time.time()
    load_file()
    get_engine_schematics()
    end = time.time()
    print(f"Time taken to run the code was {end - start} seconds")


