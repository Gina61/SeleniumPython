import configparser


def readConfigData(section, key):
    # create object of configparser
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/Config.ini")
    return config.get(section, key)

def readLocator(section, key):
    # create object of configparser
    config = configparser.ConfigParser()
    config.read("./ConfigurationFiles/ElementLocator.ini")
    return config.get(section, key)


