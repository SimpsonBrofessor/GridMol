
# ----------------------------------------------------------
#  CONSOLE LOG
#  print info to terminal on startup
# ----------------------------------------------------------
def Log(version):
    # clear terminal
    print("\033c\033[3J")
    
    print()
    print('----------------------------------')
    print('GridMol')
    print(version)
    print('Algorithm for generating new molecule from database of docked molecules')
    print('(C) Simpson College 2017')
    print('----------------------------------')
    print()
