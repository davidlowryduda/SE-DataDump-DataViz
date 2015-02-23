import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
from matplotlib.collections import LineCollection
import pickle

# Helper functions for cmap lines


def make_segments(x, y):
    points = np.array([x,y]).T.reshape(-1,1,2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    return segments


def colorline(x, y, z=None, cmap=plt.get_cmap("copper"),
              norm=plt.Normalize(0.0, 1.0), linewidth=3, alpha = 0.7):
    if z is None:
        z = np.linspace(0.0, 1.0, len(x))
    if not hasattr(z, "__iter__"):
        z = np.array([z])

    z = np.asarray(z)

    segments = make_segments(x,y)
    lc = LineCollection(segments, array=z, cmap=cmap, norm=norm,
                        linewidth=linewidth, alpha=alpha)
    ax = plt.gca()
    ax.add_collection(lc)
    return lc

#DATA_FILE = "zipf_words_sorted.pickle"
#f = open(DATA_FILE, "r")
#DATA = pickle.load(f)
#DATA_1000 = DATA[:1000]

#DATA_100 = DATA[:100]
#out_file = open("zipf_short_words.pickle", "w")
#pickle.dump(DATA_100, out_file)

short_file = open("zipf_short_words.pickle", "r")
DATA_100 = pickle.load(short_file)

labels = [x[0] for x in DATA_100]
values = [x[1] for x in DATA_100]
#labels = [x[0] for x in DATA_1000]
#values = [x[1] for x in DATA_1000]

data = {"Num_Values": pd.Series(values, index=labels)}
df = pd.DataFrame(data)

# Create figure of a given size
fig = plt.figure(figsize=(16, 12))
# Add a subplot
ax = fig.add_subplot(111)
# Set the title
ttl = "Zipf's law on Math.StackExchange"

#TODO color stuff
# Set transparency
a = 0.7
#Create a colormap
#customcmap = [(x/128.0, x/148.0, 0.05) for x in range(len(df))]
#customcmap = plt.get_cmap("copper")
#customcmap = "copper"
customcmap = [(0.822*(1 - float(x)/len(df))**8, 0.451*(1 - float(x)/len(df))**5,
               0.20*(1 - float(x)/len(df))**3) for x in range(len(df))]

# NOTICE: beware interaction of customcmap, and df.plot(colormap=) instead of
# df.plot(color=)

df["Num_Values"].plot(ax=ax, alpha=a, ylim=(0, max(df["Num_Values"])),
                      title=ttl, kind="bar", edgecolor=customcmap, color=customcmap)
#df["Num_Values"].plot(ax=ax, alpha=a, color="black")


#x = np.linspace(0,50,1000)
#y = [2*j for j in x]
#y = [1000000, 5000000, 1000000, 0]*100
#colorline(x,y)
#plt.xlim(x.min(), x.max())
#plt.ylim(y[0], y[-1])

#ax.plot(df["Num_Values"])

# Remove internal dotted lines
ax.grid(False)
# Remove plot frame (yuck)
ax.set_frame_on(False)
# Remove dotted line on axis
#ax.lines[0].set_visible(False)

# Customize title, set position, and make space for it
ax.set_title(ax.get_title(), fontsize=26, alpha=a, horizontalalignment="left")
plt.subplots_adjust(top=0.9)
ax.title.set_position((0, 1.03))
ax.xaxis.tick_bottom()

# Or this, maybe
#plt.title("Left", loc='left')

# Set x axis label location
ax.xaxis.set_label_position('bottom')
xlab = "Word"
ax.set_xlabel(xlab, fontsize=20, alpha=a, ha='left')
ax.xaxis.set_label_coords(-.05, -0.05)

ax.yaxis.set_ticks_position('none')
ax.xaxis.set_ticks_position('none')

# Customize x tick lables
xticks = labels
ax.set_xticklabels(xticks, fontsize=6, alpha=a, rotation=75)

# Customize y tick lables:
#, edgecolor="w"
yticks = [1, 1000000, 2500000, 5000000, 10000000]
ax.yaxis.set_ticks(yticks)
ax.set_yticklabels(yticks, fontsize=11, alpha=a)
#ax.yaxis.set_tick_params(pad=12)

plt.savefig("test.png", bbox_inches = "tight", dpi=300)
#plt.show()
