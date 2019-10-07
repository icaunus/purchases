1. Description.

The CLI script demo.py has been developed to perform simple statistical calculations.
It is written in Python 2.7 (b/c of the statistics module) and fetches its data from JSON files, located in the data sub-directory.
The file names can be arbitrary; important is the file extension (".json").

2. How to install Python 2.7.

If you do not have Python 2.7 installed on your computer, please visit https://www.python.org/downloads/release/python-271/ and scroll down to the Download paragraph.

3. Usage.

3. 1. Unpacking the script.

Unzip the archived script in a directory one level above the directory, containing your .json data files.
Please make sure that the name of your data directory is "data".

3. 2. Changing the settings.
Otherwise, you can change the data directory name, as well as other settings by editing their values in the demo.py source file.

3. 3. Adjusting the script access mode.

On Linux, you have to change the access mode to the script file in order to run it.
Everywhere in this document "me@mynotebook:~/demo$" is the prompt of your terminal, most probably, your BASH terminal.

Example:

me@mynotebook:~/demo$chmod 0740 demo.py

3. 4. Using the script.

3. 4. 1. Usage format.

You can apply the commands "--avg" (average), "--max" (maximum), "--median" (median) and "-min" (minimum), one at a time, to the data files.
Please always add the "./" characters in front of the script name, as on the next non-empty line.

./demo.py <--avg | --max | --median | --min>

Example:

me@mynotebook:~/demo$./demo.py --avg rocket
rocket: AVG = 203333

In this case the average value of a rocket purchase across several data files was calculated.

3. 4. 2. Unproper script usage.

If you apply an unregistered command and/or a non-existing purchase type, the program displays an error message and terminates.

Examples:

me@mynotebook:~/ac$ ./demo.py --abc airline
Usage: ./demo.py <--avg | --max | --median | --min>

me@mynotebook:~/ac$  ./demo.py --avg painting
Type painting NOT in recognized types.

me@mynotebook:~/ac$ ./demo.py --stddev trenchcoat
Type trenchcoat NOT in recognized types.