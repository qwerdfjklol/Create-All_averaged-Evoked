# Create-All_averaged-Evoked
The main file is Create all_averaged data.py
## Create all_averaged data.py
This file is a complement for Kymata-hpc. It contains a function called _"create_all_averaged_evoked"_. You can simply copy and past it at the bottom of "_preprocessing.py_" in kymata-hpc and  add 
- preprocessing.create_all_averaged_evoked(config=config)

behind the "_preprocessing.create_trials(config=config)_" line.

The function can help you average all the participants' cleaned evoked data, so that you can get an evoked file with much of the noise removed.

The averaged evoked file is saved in the path "_kymata-hpc/scripts/data/out/4_all_averaged_data/_"

__REMEMBER: You must have the correct form of grand average data before you enter this function.__ 
