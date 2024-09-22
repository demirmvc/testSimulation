#!bin/sh
cd 0
rm analytical_* error*
cd ..
rm -r postProcessing
foamListTimes -rm
pimpleFoam>log
pimpleFoam>log_postPro_0 -postProcess -time "0"
pimpleFoam>log_postPro_last -postProcess -latestTime
