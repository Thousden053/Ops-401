#!/bin/bash

# Ask the user for the number of documents they wish to create
echo "How many documents do you wish to create?"
read num_docs

# Ask the user for the base file name
echo "What should be the base name of the files?"
read base_name

# Loop through and create the files with numbered suffixes
for i in $(seq 1 $num_docs); do
    file_name="${base_name}_${i}.py"
    touch $file_name
    echo "Created file: $file_name"
done


