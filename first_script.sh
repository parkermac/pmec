#!/bin/bash

# Simple shell script.  To use it you need to navigate in the linux terminal
# to the place where it is, and then do:
# chmod u+x first_script.sh
# then type ./first_script.sh to run it.

# The top line #!/bin/bash is required for a bash shell script.  It is the equivalent of
# the .docx suffix of a Word file.

# The chmod changes the "mode" of the file so that it is executable "x" by the user "u" who is you.

# The ./ before the program is so that it knows exactly where the program you are want to execute is.
# The "." is shorthand for the current directory, so ./first_script.sh is the path to the file.
# You need to tell linux the path info because it only looks for things to execute in specific places,
# not everywhere.

# say something
echo "HI"
echo ""

# Create a directory for output.  If this already exists it will tell you so, and will
# not overwrite it.
thisdir=${PWD##*/} # OK I admit this is pretty cryptic! (found by Googling)
outdir="../"$thisdir"_output"
mkdir $outdir
echo ""

# put a file there
outfile=$outdir"/env.txt"
env > $outfile
echo "Creating "$outfile
echo ""

# search that file for a string (SHELL in this case)
while read a_line; do
  if [[ $a_line == *"SHELL"* ]] ; then
    echo $a_line
  fi
done < $outfile
echo ""

# iterate with an if statement
counter=0
while [ $counter -le 10 ]; do
  if [ $counter -ge 5 ]; then
    echo $counter
  fi
  (( counter++ ))
  # counter=$[$counter + 1] # this works too
done
echo ""
