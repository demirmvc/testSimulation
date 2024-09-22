#!/bin/sh



mkdir -p results_temporal

schemes="backward"

for scheme in $schemes; do
    mkdir -p results_temporal/$scheme
    
    if [ "$scheme" = "CrankNicolson" ]; then
        sed -i "19 s/.*/    default    $scheme 1;/" TGV_temporal/system/fvSchemes
    else
        sed -i "19 s/.*/    default    $scheme;/" TGV_temporal/system/fvSchemes
    fi

    echo "Running scheme: $scheme"

    for i in 0.03 0.015 0.0075 0.00375; do
           echo "  Running case with timestep: $i"

        mkdir -p results_temporal/$scheme/deltaT_$i
        sed -i "27 s/.*/deltaT    $i;/" TGV_temporal/system/controlDict
        cd TGV_temporal || exit
        bash automated.sh
        cp -r postProcessing  0.3* log* system constant weightedAverageResults.csv ../results_temporal/$scheme/deltaT_$i/
        bash deleteall.sh
        cd ..
    done
done
