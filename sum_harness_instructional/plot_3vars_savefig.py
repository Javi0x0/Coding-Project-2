import pandas as pd
import matplotlib.pyplot as plt

plot_mflops_fname = "mflops_plot.png"
plot_bandwidth_fname = "bandwidth_plot.png"
plot_latency_fname = "latency_plot.png"

fname = "sample_data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

# Assuming the first column is Problem Size and the rest are timing data
problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()

MEMORY_BANDWIDTH_CAPACITY = 204.8 * 10**9  #(204.8 GB/s)

def calculate_mflops(problem_sizes, elapsed_times):
    mflops = []
    for size, time in zip(problem_sizes, elapsed_times):
        # MFLOP/s = (N)/(Elapsed Time in seconds * 10^6)
        mflops_value = (size) / (time * 10**6)  # Using size - 1 for better accuracy
        mflops.append(mflops_value)
    return mflops

code1_mflops = calculate_mflops(problem_sizes, code1_time)
code2_mflops = calculate_mflops(problem_sizes, code2_time)
code3_mflops = calculate_mflops(problem_sizes, code3_time)

# Calculate % bandwidth and memory latency
def calculate_bandwidth(problem_sizes, elapsed_times):
    bandwidth = []
    for size, time in zip(problem_sizes, elapsed_times):
        # Bandwidth = (bytes accessed/time in seconds)/capacity
        # For simplicity, we assume bytes accessed = size * 8 (since each uint64_t is 8 bytes)
        bytes_accessed = size * 8
        bandwidth_value = (bytes_accessed / time)/MEMORY_BANDWIDTH_CAPACITY  # in bytes/sec
        bandwidth.append(bandwidth_value)
    return bandwidth

def calculate_memory_latency(elapsed_times, problem_sizes):
    latency = []
    for time, size in zip(elapsed_times, problem_sizes):
        # Memory latency in nanoseconds
        latency_value = (time / size) * 10**9  # converting seconds to nanoseconds
        latency.append(latency_value)
    return latency

code1_bandwidth = calculate_bandwidth(problem_sizes, code1_time)
code2_bandwidth = calculate_bandwidth(problem_sizes, code2_time)
code3_bandwidth = calculate_bandwidth(problem_sizes, code3_time)

code1_latency = calculate_memory_latency(code1_time, problem_sizes)
code2_latency = calculate_memory_latency(code2_time, problem_sizes)
code3_latency = calculate_memory_latency(code3_time, problem_sizes)

# Print results for MFLOP/s
print("MFLOP/s Results:")
print("Problem Size | Direct MFLOP/s | Indirect MFLOP/s | Vector MFLOP/s")
for i in range(len(problem_sizes)):
    print(f"{problem_sizes[i]:<13} | {code1_mflops[i]:<15.2f} | {code2_mflops[i]:<16.2f} | {code3_mflops[i]:<14.2f}")

# Print results for Memory Bandwidth
print("\nMemory Bandwidth Results (bytes/sec):")
print("Problem Size | Direct Bandwidth | Indirect Bandwidth | Vector Bandwidth")
for i in range(len(problem_sizes)):
    print(f"{problem_sizes[i]:<13} | {code1_bandwidth[i]:<17.2f} | {code2_bandwidth[i]:<18.2f} | {code3_bandwidth[i]:<16.2f}")

# Print results for Memory Latency
print("\nMemory Latency Results (ns):")
print("Problem Size | Direct Latency | Indirect Latency | Vector Latency")
for i in range(len(problem_sizes)):
    print(f"{problem_sizes[i]:<13} | {code1_latency[i]:<14.2f} | {code2_latency[i]:<15.2f} | {code3_latency[i]:<13.2f}")

# Plot MFLOP/s
plt.figure()
plt.title("MFLOP/s")
xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, problem_sizes)

plt.plot(code1_mflops, "r-o", label="Sum Direct MFLOP/s")
plt.plot(code2_mflops, "b-x", label="Sum Indirect MFLOP/s")
plt.plot(code3_mflops, "g-^", label="Sum Vector MFLOP/s")

plt.xlabel("Problem Sizes")
plt.ylabel("MFLOP/s")
plt.legend(loc="best")
plt.grid(axis='both')
plt.savefig(plot_mflops_fname, dpi=300)
plt.show()

# Plot % of Bandwidth
plt.figure()
plt.title("Bandwidth")
plt.xticks(xlocs, problem_sizes)

plt.plot(code1_bandwidth, "r-o", label="Direct Sum Bandwidth")
plt.plot(code2_bandwidth, "b-x", label="Indirect Sum Bandwidth")
plt.plot(code3_bandwidth, "g-^", label="Vector Sum Bandwidth")

plt.xlabel("Problem Sizes")
plt.ylabel("% of Bandwidth used")
plt.legend(loc="best")
plt.grid(axis='both')
plt.savefig(plot_bandwidth_fname, dpi=300)
plt.show()

# Plot Memory Latency (ns)
plt.figure()
plt.title("Memory Latency")
plt.xticks(xlocs, problem_sizes)

plt.plot(code1_latency, "r-o", label="Direct Sum Latency (ns)")
plt.plot(code2_latency, "b-x", label="Indirect Sum Latency (ns)")
plt.plot(code3_latency, "g-^", label="Vector Sum Latency (ns)")

plt.xlabel("Problem Sizes")
plt.ylabel("Latency (ns)")
plt.legend(loc="best")
plt.grid(axis='both')
plt.savefig(plot_latency_fname, dpi=300)
plt.show()

# EOF
