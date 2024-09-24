#!/bin/bash

# Find all process_delta_folders.sh files and execute them
find . -type f -name "process_delta_folders.sh" | while read -r script; do
    echo "Running script: $script"  # Print the path of the script being executed
    
    # Get the directory where the script is located
    script_dir=$(dirname "$script")

    # Change to the directory where the script is located
    cd "$script_dir" || { echo "Failed to enter directory: $script_dir"; continue; }

    # Execute the script and capture both standard output and standard error
    output=$(bash "$(basename "$script")" 2>&1)

    # Print the output of the script
    echo "Output of script $script:"
    echo "$output"
    echo "-----------------------------------------"
    echo "Finished running script: $script"  # Indicate completion
    echo "-----------------------------------------"

    # Return to the original directory
    cd - > /dev/null
done

