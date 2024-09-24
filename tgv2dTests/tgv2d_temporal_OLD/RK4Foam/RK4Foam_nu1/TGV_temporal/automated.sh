#!bin/sh
cd 0
rm analytical_* error*
cd ..
rm -r postProcessing
foamListTimes -rm
RK4Foam>log
RK4Foam>log_postPro_0 -postProcess -time "0"
RK4Foam>log_postPro_last -postProcess -latestTime
