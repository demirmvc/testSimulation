#!/bin/bash

# Extract time values
grep '^Time =' log | awk '{print $3}' > time.dat

# Extract residual values for each variable
grep 'Solving for Ux,' log | awk '{print $8}' | tr -d , > ux.dat
grep 'Solving for Uy,' log | awk '{print $8}' | tr -d , > uy.dat
grep 'Solving for Uz,' log | awk '{print $8}' | tr -d , > uz.dat
grep 'Solving for p,' log | awk 'NR%2==0 {print $8}' | tr -d , > pr.dat

# Combine time with each residual
paste time.dat ux.dat > time_ux.dat
paste time.dat uy.dat > time_uy.dat
paste time.dat uz.dat > time_uz.dat
paste time.dat pr.dat > time_pr.dat

