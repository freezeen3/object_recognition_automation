To set up the environment to run this script:

1. Open anaconda shell (conda_dir) preferably with admin right if you are to install any package
(otherwise the packages would go into the C: drive .conda hidden directory and we do not want to
  occupy C: drive spaces)

2. Check if our osrs env is present in conda with:
conda env list

3. Navigate to our working directory if not already in:
E:
cd ml_test\osrs_auto

4. Activate the desired environment (osrs here):
conda activate osrs

5. Now you can freely run the python scripts with:
python fisher.py

Check the installed packages of this environment with:
conda list

Use the following to check if a particular package is here:
conda list <packagename>

It is normal that conda env list, conda list commands would take a while to process
