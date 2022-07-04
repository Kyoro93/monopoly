from collections import Counter


def show_statistics(results):
    '''
    ### Exit
    A execution of a program that runs 300 simulations and
    print into the console their results. The expected results
    are shown below:

    * How many games finished by "timeout" (1000 rounds);

    * How many shifts on average a simulation needs to end;

    * Whats the percentage of victory of each player's behavior;

    * What's the behavior that wins the most.
    '''
    total_timeout = sum([1 for result in results if result["time_out"]])
    # total_time = sum([result["time_it"] for result in results])
    total_played = sum([result["played"] for result in results])
    count_winner = Counter()
    for result in results:
        behavior = str(result['behavior'])
        count_winner[behavior] += 1
    # quantos turnoe em media demora uma partida
    print(
        f'''How many games ended by timeout: '''
        f'''{total_timeout}'''
    )
    print(
        f'''How many shift on average a match takes to end: '''
        f'''{total_played / len(results):.1f}'''
    )
    print(
        f'''What's the behavior that most win:
        {count_winner.most_common(1)[0][0]}
        won: {count_winner.most_common(1)[0][1]}'''
    )
    print("What's the percentage of victories per player's behavior")
    for behavior, winner in count_winner.most_common():
        print("  *  ", f"{behavior}: {(winner * 100)// len(results)}%")
