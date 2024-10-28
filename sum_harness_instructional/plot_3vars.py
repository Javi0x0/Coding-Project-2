"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt


fname = "sample_data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()

def calculate_mflops(problem_sizes, elapsed_times):
    mflops = []
    for size, time in zip(problem_sizes, elapsed_times):
        # MFLOP/s = (N - 1) / (Elapsed Time in seconds * 10^6)
        mflops_value = (size - 1) / (time * 10**6)  # Using size - 1 for better accuracy
        mflops.append(mflops_value)
    return mflops

code1_mflops = calculate_mflops(problem_sizes, code1_time)
code2_mflops = calculate_mflops(problem_sizes, code2_time)
code3_mflops = calculate_mflops(problem_sizes, code3_time)

plt.figure()
plt.title("Comparison of 3 Codes - MFLOP/s")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

# here, we are plotting the raw values read from the input .csv file, which
# we interpret as being "time" that maps directly to the y-axis.
#
# what if we want to plot MFLOPS instead? How do we compute MFLOPS from
# time and problem size? You may need to add some code here to compute
# MFLOPS, then modify the plt.plot() lines below to plot MFLOPS rather than time.

# Plotting MFLOP/s values instead of raw elapsed times
plt.plot(code1_mflops, "r-o", label="Sum Direct MFLOP/s")
plt.plot(code2_mflops, "b-x", label="Sum Indirect MFLOP/s")
plt.plot(code3_mflops, "g-^", label="Sum Vector MFLOP/s")

#plt.xscale("log")  # Optional: Log scale for better visualization
#plt.yscale("log")  # Optional: Log scale for better visualization

plt.xlabel("Problem Sizes")
plt.ylabel("MFLOP/s")
plt.legend(loc="best")
plt.grid(axis='both')

# Display the plot
plt.show()

# EOF
