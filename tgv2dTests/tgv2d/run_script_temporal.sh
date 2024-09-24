#!/bin/sh


# RUN FOR RE = 100
mkdir -p results_temporal

schemes="rk4Foam RK4Foam rk4fracsFoam"
for scheme in $schemes; do
    mkdir -p results_temporal/$scheme
    echo "Running solver ...: $scheme"
    sed -i "7 s/.*/ $scheme > log/" TGV_temporal/automated.sh
    sed -i "8 s/.*/$scheme > log_postPro_0 -postProcess -time '0'/" TGV_temporal/automated.sh
sed -i "9 s/.*/ $scheme > log_postPro_last -postProcess -lastestTime/" TGV_temporal/automated.sh


    for i in 0.001 0.0001 0.00001; do
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
