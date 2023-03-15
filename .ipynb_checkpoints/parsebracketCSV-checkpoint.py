import csv

number_of_games = 63
filesrc = 'NCAAMensMarchMadnessHistoricalResults.csv'
filedst = 'SeedsVSRounds.csv'
DEBUG = False

def export(data):
    with open(filedst, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def round(str):
    if str == 'Round of 64':
        return 1
    elif str == 'Round of 32': 
        return 2
    elif str == 'Sweet Sixteen':
        return 3
    elif str == 'Elite Eight':
        return 4
    elif str == 'National Semifinals':
        return 5
    elif str == 'National Championship':
        return 6 #handle 6 to check if that seed is the winner or loser, winner gets a 'round score' of 7
    elif str == 'Opening Round':
        return -1


'''
year is a 4 digit paramter marking the year of that specific tournament
'''
def year(yr):
    with open(filesrc, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        loser_index = 6
        round_index = 1
        winner_index = 3

        
        offset = 63 * (yr-1985) # this is how far we need to move from the first row
        for i in range(offset):
            try:
                row = next(reader)
            except StopIteration:
                print(StopIteration)
                return 
            
        #                                                                                            |
        #we have ignored our irrelevant data for each year and can process that years data following |
        #                                                                                            v    


        rows = []
        data = [['Seed', 'Games']]
        for i in range(number_of_games):
            try:
                row = next(reader)
                round_int = round(row[round_index])
                
                entry = [int(row[loser_index]), round_int]
                if round_int != -1: 
                    data.append(entry)
                if round_int == 6:
                    entry2 = [int(row[winner_index]), 7]
                    data.append(entry2)
            except StopIteration:
                break
            rows.append(row) 
        # Process the current chunk of rows here
        if DEBUG:
            print(str(yr) + ": " + str(data) + "\n")

        return data[1:]


def main():
    # Your code here
    yr = 1985
    data = [['Seed', 'Games']]
    while yr < 2016:
        for entry in year(yr):
            data.append(entry)
        yr+=1
    export(data)

if __name__ == "__main__":
    main()