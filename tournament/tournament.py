def tally(rows):
    output = []
    team_records = dict()
    header = 'Team                           | MP |  W |  D |  L |  P'
    output.append(header)

    for row in rows:
        game_result : dict = parse_row_of_summary(row)

        winning_team = game_result.get('winner')

        # If the game was a draw, there would not be a winner (or a loser for that matter).
        if winning_team is not None:
            losing_team = game_result['loser']

            # Is there already an entry for the winning and losing team in the team_records dict?
            # IF so, append the correct game result to it.
            # If not, then create the array that will keep track of that team's game results.

            if winning_team in team_records:
                team_records[winning_team].append('W')

            else:
                team_records[winning_team] = ['W']


            if losing_team in team_records:
                team_records[losing_team].append('L')

            else:
                team_records[losing_team] = ['L']


        else:
            teams_that_played = game_result['drawers']

            for team in teams_that_played:
                if team in team_records:
                    team_records[team].append('D')

                else:
                    team_records[team] = ['D']


    # A lot to unpack here. Basically we are constructing a sorted representation of the dictionary,
    # using two things: 1) the points value, 2) alphabetical order of the keys.
    # The key variable here is a tuple where the first element (0) is the key name itself, and the second
    # element (1) is it's value.
    # For the first sort, use map to transform the array of letters into numerical points, and then
    # sum over that to get the total points. Because sorted() by default sorts in ascending order, we
    # negate the points to create a descending order. (More on this later..)
    # For the second sort, simply pass the name of the key itself to use an alphabetical sort.
    #
    # Also, one gotcha here is that it seems like you can't quite use the 'reverse=True' argument
    # to sorted() unless you also negate the second argument in the lambda (which handles alphabetical sort)
    for team in sorted(team_records.items(), key= lambda k :  (-sum(map(assign_points_to_game_result, k[1])), k[0])):
        team_name, team_record = team
        team_results = compute_statistics_for_record(team_record)
        output.append(construct_string_for_results(team_name,
                                                   team_results['matches_played'],
                                                   team_results['wins'],
                                                   team_results['draws'],
                                                   team_results['losses'],
                                                   team_results['total_points']))


    return output


def assign_points_to_game_result(result : str) -> int:
    if (result == 'W'):
        return 3

    elif (result == 'L'):
        return 0

    elif (result == 'D'):
        return 1


def parse_row_of_summary(line : str) -> dict:
    record = dict()
    team1, team2, result = line.split(";")

    # Per the instructions, the result applies to the first team if its a win or a loss.
    if (result == "win"):
        record['winner'] = team1
        record['loser'] = team2

    elif (result == "loss"):
        record['winner'] = team2
        record['loser'] = team1

    elif (result == "draw"):
        record['drawers'] = [team1, team2]

    return record

def compute_statistics_for_record(record : list) -> dict:
    results = {}

    results['matches_played'] = len(record)
    results['wins'] = record.count('W')
    results['losses'] = record.count('L')
    results['draws'] = record.count('D')
    # TODO: This value was already computed once, figure out a clean way to use it from earlier.
    results['total_points'] = sum(map(assign_points_to_game_result, record))

    return results

def construct_string_for_results(team_name, matches_played, wins, draws, losses, points) -> str:
    line_of_result = ""
    line_of_result += team_name

    # The header specifies that the team name space has to occupy 31 characters.
    line_of_result += ((31 - len(team_name)) * " ")
    line_of_result += "|"

    line_of_result += f"  {matches_played} |  {wins} |  {draws} |  {losses} |  {points}"
    return line_of_result
