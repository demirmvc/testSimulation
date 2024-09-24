#!bin/sh
cd 0
rm analytical_* error*
cd ..
rm -r postProcessing
foamListTimes -rm
 rk4Foam > log
rk4Foam > log_postPro_0 -postProcess -time '0'
 rk4Foam > log_postPro_last -postProcess -lastestTime
