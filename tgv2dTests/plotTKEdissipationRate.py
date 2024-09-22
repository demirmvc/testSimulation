import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import itertools

def normalize_by_max(df, columns):
    for column in columns:
        max_value = df[column].max()
        df[column] = df[column] / max_value
    return df


def sample_data(df, num_samples=20):
    if len(df) > num_samples:
        return df.iloc[::max(len(df) // num_samples, 1), :]
    else:
        return df


columns = ["TKE","dissipationRate"]

base_dir = "/home/hakan/courses/testSimulation/tgv2dTests/tgv2d_temporal_pimple/results_temporal/"

scenarios = {
    "linear CrankNicolson": "CrankNicolson",
    "linear backward": "backward",
    "cubic CrankNicolson": "CrankNicolson",
    "cubic backward": "backward",
}

deltaT_values = ["deltaT_0.0000125", "deltaT_0.000025", "deltaT_0.00005", "deltaT_0.0001"]

colors = itertools.cycle(plt.cm.tab10.colors)
line_styles = itertools.cycle(['-', '--', '-.', ':'])
markers = itertools.cycle(['o', 's', 'D', '^', 'v', '<', '>', 'p', 'h'])

data_storage = pd.DataFrame(columns=["scenario", "deltaT", "time", "TKE", "dissipationRate"])

fig_128, tgv2d = plt.subplots(2, 1, figsize=(10, 8))

for scenario, sub_dir in scenarios.items():
    for deltaT in deltaT_values:
        color = next(colors)
        line_style = next(line_styles)
        marker = next(markers)

        # Build the file path for the weightedAverageResults.csv file
        file_path = os.path.join(base_dir, sub_dir, deltaT, "weightedAverageResults.csv")
        
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            
            # Drop the last 2 rows from the dataframe
            if len(df) > 2:
                df = df.iloc[:-2]
            else:
                print(f"Not enough data to drop last 2 rows in file: {file_path}")
                continue
            
            # Sample and normalize the remaining data
            df = sample_data(df)
            df_normalized = normalize_by_max(df, columns)
            
            TKE = np.abs(df_normalized["TKE"])
            dissipationRate = np.abs(df_normalized["dissipationRate"])
        
      
            tgv2d[0].plot(df["time"], TKE, label=f"{scenario} - {deltaT}", color=color, linestyle=line_style, marker=marker)
            tgv2d[1].plot(df["time"], dissipationRate, label=f"{scenario} - {deltaT}", color=color, linestyle=line_style, marker=marker)
                
                # Store the results in the data_storage DataFrame
            temp_df = pd.DataFrame({
                    "scenario": scenario,
                    "deltaT": deltaT,
                    "time": df["time"],
                    "TKE": TKE,
                    "dissipationRate": dissipationRate
            })
            data_storage = pd.concat([data_storage, temp_df], ignore_index=True)


tgv2d[0].set_title('TGV 128')
tgv2d[0].set_xlabel('Time')
tgv2d[0].set_ylabel(r'$K/K_0$')
tgv2d[0].legend()

tgv2d[1].set_title('TGV 128')
tgv2d[1].set_xlabel('Time')
tgv2d[1].set_ylabel(r'$\epsilon/\epsilon_{max}$')
tgv2d[1].legend()


