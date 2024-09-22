#!bin/sh
cd 0
rm analytical_* error*
cd ..
rm -r postProcessing
foamListTimes -rm
erkFoam>log
erkFoam>log_postPro_0 -postProcess -time "0"
erkFoam>log_postPro_last -postProcess -latestTime
