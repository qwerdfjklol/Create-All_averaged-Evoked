from colorama import Fore
from colorama import Style
import matplotlib.pyplot as plt
import mne
import os.path
import sklearn
import seaborn as sns
import numpy as np

import utils


def create_all_averaged_evoked(config: dict):
    """Create averaged evoked objects from the cleaned evoked data files (still in sensor space)"""

    list_of_participants = config['list_of_participants']

    print(f"{Fore.GREEN}{Style.BRIGHT}Starting program and {Style.RESET_ALL}")

    all_evoked_data = []

    for p in list_of_participants:

        print(f"{Fore.GREEN}{Style.BRIGHT}...extracting files{Style.RESET_ALL}")

        averaged_fname = 'data/out/3_evoked_sensor_data/evoked_grand_average/' + p + '-grandave.fif'

        grand_average_data = mne.read_evokeds(averaged_fname)

        all_evoked_data.append(grand_average_data[0])

    print(f"{Fore.GREEN}{Style.BRIGHT}...averaging evoked{Style.RESET_ALL}")

    evoked_grand_average = mne.combine_evoked(all_evoked_data, 'nave')

    print(f"{Fore.GREEN}{Style.BRIGHT}...save all average{Style.RESET_ALL}")

    evoked_grand_average.save('data/out/4_all_averaged_data/meg15_all_ave.fif', overwrite=True)