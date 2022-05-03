#-------------- Victor --------------#
class c:
    # Args to test w/out graphics and for 1000 games
    ARGS = ['-p', 'PacmanDQN', '-n', '1001', '-x', '1', '-q']

    # directory/file locations
    
    ############## SMALL CLASSIC ################ 
    SMALL_CLASSIC_FOLDER = 'C:/Users/GoncalvesVictorEduar/Desktop/Pacman/saves/smallClassic/'
    # SMALL_CLASSIC_FOLDER = 'C:/Users/vg210/Desktop/Pacman/saves/smallClassic/'

    # Control: 100k smallClassic DirectionalGhost
    SMALL_CLASSIC_DIRECTIONAL = 'model-smallClassic_5860553_24626'

    # Random: 100k smallClassic + 30k RandomGhost
    SMALL_CLASSIC_RANDOM = 'model-smallClassic_8698647_26605'

    # Half-and-Half: 100k smallClassic + 30k half/half
    SMALL_CLASSIC_HALF_HALF = 'model-smallClassic_8195775_29837'

    # Less Ghosts: 100k smallClassic + 30k less ghosts
    SMALL_CLASSIC_ONE_GHOST = 'model-smallClassic_7455700_29929'

    # Experiments list: (file location, args)

    # Experiments against respective environment
    SMALL_CLASSIC_EXPERIMENTS = [(SMALL_CLASSIC_DIRECTIONAL, ARGS + ['-g', 'DirectionalGhost', '-l', 'smallClassic']), 
                                 (SMALL_CLASSIC_RANDOM, ARGS + ['-g', 'RandomGhost', '-l', 'smallClassic']), 
                                 (SMALL_CLASSIC_HALF_HALF, ARGS + ['-g', 'HalfAndHalf', '-l', 'smallClassic']), 
                                 (SMALL_CLASSIC_ONE_GHOST, ARGS + ['-g', 'DirectionalGhost', '-l', 'smallClassicOneGhost'])]

    # Experiments against control environment
    SMALL_CLASSIC_EXPERIMENTS_ON_CONTROL = [(SMALL_CLASSIC_DIRECTIONAL, ARGS + ['-g', 'DirectionalGhost', '-l', 'smallClassic']), 
                                 (SMALL_CLASSIC_RANDOM, ARGS + ['-g', 'DirectionalGhost', '-l', 'smallClassic']), 
                                 (SMALL_CLASSIC_HALF_HALF, ARGS + ['-g', 'DirectionalGhost', '-l', 'smallClassic']), 
                                 (SMALL_CLASSIC_ONE_GHOST, ARGS + ['-g', 'DirectionalGhost', '-l', 'smallClassic'])]

    ################ SMALL GRID ################## 
    SMALL_GRID_FOLDER = 'C:/Users/GoncalvesVictorEduar/Desktop/Pacman/saves/smallGrid/'
    # SMALL_GRID_FOLDER = 'C:/Users/vg210/Desktop/Pacman/saves/smallGrid/'

    # Control: 100k smallGrid DirectionalGhost 
    SMALL_GRID_DIRECTIONAL = 'model-smallGrid_2735611_100878'

    # Random: 100k smallGrid + 30k RandomGhost
    SMALL_GRID_RANDOM = 'model-smallClassic_3270774_30084'

    # Half-and-Half: 100k smallGrid + 30k half/half
    SMALL_GRID_HALF_HALF = 'model-smallClassic_3271349_29522'

    # More Pebbles: 100k smallGrid + 30k more pebbles
    SMALL_GRID_MORE_PEBBLES = 'model-smallClassic_3380835_30071'

    # Experiments list: (file location, args)

    # Experiments against respective environment
    SMALL_GRID_EXPERIMENTS = [(SMALL_GRID_DIRECTIONAL, ARGS + ['-g', 'DirectionalGhost', '-l', 'smallGrid']), 
                                 (SMALL_GRID_RANDOM, ARGS + ['-g', 'RandomGhost', '-l', 'smallGrid']), 
                                 (SMALL_GRID_HALF_HALF, ARGS + ['-g', 'HalfAndHalf', '-l', 'smallGrid']), 
                                 (SMALL_GRID_MORE_PEBBLES, ARGS + ['-g', 'DirectionalGhost', '-l', 'smallGridMorePebbles'])]

    # Experiments against control environment
    SMALL_GRID_EXPERIMENTS_ON_CONTROL = [(SMALL_GRID_DIRECTIONAL, ARGS + ['-g', 'DirectionalGhost', '-l', 'smallGrid']), 
                                 (SMALL_GRID_RANDOM, ARGS + ['-g', 'DirectionalGhost', '-l', 'smallGrid']), 
                                 (SMALL_GRID_HALF_HALF, ARGS + ['-g', 'DirectionalGhost', '-l', 'smallGrid']), 
                                 (SMALL_GRID_MORE_PEBBLES, ARGS + ['-g', 'DirectionalGhost', '-l', 'smallGrid'])]
    

