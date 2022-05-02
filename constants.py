#-------------- Victor --------------#
from pickle import NONE


class c:
    # Different Experiments
    DIRECTIONAL = 1
    RANDOM = 2
    HALF_HALF = 3
    ONE_GHOST = 4
    MORE_PEBBLES = 5

    ARGS = ['-p', 'PacmanDQN', '-n', '1001', '-x', '1', '-q']
'-l', 'smallGrid',
'-g', 'DirectionalGhost', 
    
    # directory/file locations
    
    ############## SMALL CLASSIC ################ 
    SMALL_CLASSIC_FOLDER = 'Pacman\saves\smallClassic'

    # Control: 100k smallClassic DirectionalGhost
    SMALL_CLASSIC_DIRECTIONAL = 'smallClassic100kControl'

    # Random: 100k smallClassic + 30k RandomGhost
    SMALL_CLASSIC_RANDOM = 'smallClassic30kRandom'

    # Half-and-Half: 100k smallClassic + 30k half/half
    SMALL_CLASSIC_HALF_HALF = 'smallClassic30kHalf&Half'

    # Less Ghosts: 100k smallClassic + 30k less ghosts
    SMALL_CLASSIC_ONE_GHOST = 'smallClassic30k1Ghost'

    # Experiments list
    SMALL_CLASSIC_EXPERIMENTS = [SMALL_CLASSIC_DIRECTIONAL, SMALL_CLASSIC_RANDOM, SMALL_CLASSIC_HALF_HALF, SMALL_CLASSIC_ONE_GHOST, NONE]

    ################ SMALL GRID ################## 
    SMALL_GRID_FOLDER = 'Pacman\saves\smallGrid'

    # Control: 100k smallGrid DirectionalGhost 
    SMALL_GRID_DIRECTIONAL = 'smallGrid100kControl'

    # Random: 100k smallGrid + 30k RandomGhost
    SMALL_GRID_RANDOM = 'smallGrid30kRandom'

    # Half-and-Half: 100k smallGrid + 30k half/half
    SMALL_GRID_HALF_HALF = 'smallGrid30kMorePebbles'

    # More Pebbles: 100k smallGrid + 30k more pebbles
    SMALL_GRID_MORE_PEBBLES = 'smallGrid30kMorePebbles'

    # Experiments list
    SMALL_GRID_EXPERIMENTS = [SMALL_GRID_DIRECTIONAL, SMALL_GRID_RANDOM, SMALL_GRID_HALF_HALF, NONE, SMALL_GRID_MORE_PEBBLES]

