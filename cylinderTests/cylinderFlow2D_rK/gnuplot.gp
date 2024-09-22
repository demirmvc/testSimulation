# Configure the plot settings
set logscale y  # Set y-axis to logarithmic scale
set xlabel 'Time, s'  # Label for x-axis
set ylabel 'Residual'  # Label for y-axis

set ytics nomirror format "%.0e"  # Set y-axis ticks format

# Plot the data with different line styles and titles
plot 'time_ux.dat' using 1:2 w l ls 1 lw 2 title 'ux residual', \
     'time_uy.dat' using 1:2 w l ls 2 lw 2 title 'uy residual', \
     'time_uz.dat' using 1:2 w l ls 3 lw 2 title 'uz residual', \
     'time_pr.dat' using 1:2 w l ls 4 lw 2 title 'pressure residual'

pause(-1)  # Pause to view the plot

