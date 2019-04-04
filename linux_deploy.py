#code goes here
import subprocess
import os
from termcolor import colored

skipped_steps = 0
changed_steps = 0


FNULL = open(os.devnull, 'w')

#Create deploy_directory if not already there

directory_present = True

try:
    subprocess.check_call(["ls", "deploy_directory"], stdout=FNULL, stderr=subprocess.STDOUT)
except subprocess.CalledProcessError:
    directory_present = False

if directory_present == False:
    subprocess.call(["mkdir", "deploy_directory"])
    changed_steps += 1
    print('\n[Create deploy_directory]') + colored('\nChanged: Created deploy_directory.\n', 'yellow')
else:
    skipped_steps += 1
    print('\n[Create deploy_directory]') + colored('\nSkipped: Directory already here.\n', 'green')

#Copy newfile.txt to deploy_directory is newfile.txt is different than what is already there

newfile_exists = True

try:
    subprocess.check_call(["cat", "deploy_directory/newfile.txt"], stdout=FNULL, stderr=subprocess.STDOUT)

except subprocess.CalledProcessError:
    newfile_exists = False

if newfile_exists == False:

    subprocess.call(["cp", "newfile.txt", "deploy_directory"])
    changed_steps += 1
    print('\n[Copy newfile.txt]') + colored('\nChanged: newfile.txt copied.\n', 'yellow')

else:
    proc = subprocess.Popen(["diff", "newfile.txt", "deploy_directory/newfile.txt"], stdout=subprocess.PIPE)
    newfile_diff = proc.stdout.read()
    
    if len(newfile_diff) != 0:
        subprocess.call(["rm", "deploy_directory/newfile.txt"])
        subprocess.call(["cp", "newfile.txt", "deploy_directory"])
        changed_steps +=1
        print('\n[Copy newfile.txt]') + colored('\nChanged: newfile.txt was different so it was copied.', 'yellow')

    else:
        print('\n[Copy newfile.txt]') + colored('\nSkipped: File already exists.\n', 'green')
        skipped_steps += 1

print colored('\nSkipped: ', 'green') + colored(skipped_steps, 'green') + colored('  Changed: ', 'yellow') + colored(changed_steps, 'yellow')


