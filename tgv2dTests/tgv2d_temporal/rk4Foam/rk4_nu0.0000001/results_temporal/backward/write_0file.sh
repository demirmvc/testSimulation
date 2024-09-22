#!/bin/sh


cd deltaT_0.03/
rk4Foam > log_0 -postProcess -time "0"
cd ..
cd deltaT_0.015/
rk4Foam > log_0 -postProcess -time "0"
cd ..
cd deltaT_0.0075/
rk4Foam > log_0 -postProcess -time "0"
cd ..
cd deltaT_0.00375/
rk4Foam > log_0 -postProcess -time "0"
cd ..
