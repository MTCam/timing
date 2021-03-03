import yaml
import pandas as pd
import matplotlib.pyplot as plt

# load the data
data = yaml.load_all(open('y1-nozzle-timings.yaml', 'r'), Loader=yaml.FullLoader)
data = [d for d in list(data) if d is not None]
df = pd.DataFrame(data)
df['run_date'] = pd.to_datetime(df['run_date'], errors='coerce')

# plot
fig, ax = plt.subplots(figsize=(10,5))
kwargs = {'marker': 'o',
          'ms': 5,
          'markerfacecolor': 'w',
          'linestyle': '-',
          'linewidth': 2,
         }

for s in ['time_startup', 'time_first_10', 'time_second_10']:
    ax.plot(df['run_date'], df[s], label=s.replace('time_',''), **kwargs)

ax.tick_params(axis='x', labelrotation = 45)
ax.grid(True)
ax.set_xlabel('date')
ax.set_ylabel('time (s)')
ax.legend()
plt.show()
