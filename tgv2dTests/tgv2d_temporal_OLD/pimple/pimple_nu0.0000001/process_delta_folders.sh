#!/bin/bash

folders=("Euler" "backward" "CrankNicolson")

for folder in "${folders[@]}"; do
    echo "Processing folder: $folder"
    if [ -d "$folder" ]; then
        cd "$folder" 

        for delta_folder in deltaT_*; do
            if [ -d "$delta_folder" ]; then
                echo "  Processing delta folder: $delta_folder"
                cd "$delta_folder"
                
                if [ -d "postProcessing/error_velocity_norm/0" ]; then
                    cd "postProcessing/error_velocity_norm/0" 

                    if [ -f "volFieldValue_0.dat" ]; then
                        echo "    Found volFieldValue_0.dat in $folder/$delta_folder"
                        
                        # Extracting the max error velocity magnitude from the file
                        max_error_velocity=$(grep -v "#" volFieldValue_0.dat | awk '{print $2}')
                        echo "    Max Error Velocity Magnitude: $max_error_velocity"
                    else
                        echo "    volFieldValue_0.dat not found in $folder/$delta_folder"
                    fi

                    cd ../../../..  # Go back to the folder level
                else
                    echo "    Directory postProcessing/error_velocity_norm/0 does not exist in $folder/$delta_folder"
                    cd ../..  # Go back to the folder level
                fi
                 
            else
                echo "  Delta folder $delta_folder does not exist in $folder"
            fi
        done
        
        cd ..  # Go back to base directory
        echo "****************************************************"
        echo "                                                    "

    else
        echo "Folder $folder does not exist!"
    fi
done
