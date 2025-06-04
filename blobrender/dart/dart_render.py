import argparse
import yaml 
import numpy as np
import matplotlib.pyplot as plt
import os

from ..import tools
from ..paths import CONFIGS
from blobrender.help_strings import HELP_DICT
from blobrender.dart import dart as dt

def main():

    yaml_file = os.path.join(CONFIGS, "default_dart_render.yaml")
    def_args = tools.get_arguments(yaml_file, HELP_DICT)

    load_str = args.load_str
    expand_grid = args.expand_grid
    


if __name__ == "__main__":
    main()