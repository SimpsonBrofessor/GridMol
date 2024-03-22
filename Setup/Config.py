import yaml

# ----------------------------------------------------------
#  CONFIGURATION SETUP
#  load yaml config file 
# ----------------------------------------------------------
def Config(filename):
    try:
        with open(filename, 'r') as ymlfile:
            return yaml.load(ymlfile, yaml.SafeLoader)
        
    except:
        print("CONFIGURATION FILE NOT FOUND: {}".format(filename))
