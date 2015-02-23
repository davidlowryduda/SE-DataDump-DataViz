
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
from matplotlib.collections import LineCollection


labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
values = [1, 2, 3, 5, 7, 9, 10]

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
customcmap = [(x/24.0, x/48.0, 0.05) for x in range(len(df))]
#customcmap = plt.get_cmap("copper")

# NOTICE: beware interaction of customcmap, and df.plot(colormap=) instead of
# df.plot(color=)

df["Num_Values"].plot(ax=ax, alpha=a, ylim=(0, max(df["Num_Values"])),
                      title=ttl, kind="bar", edgecolor="w", color=customcmap)
#df["Num_Values"].plot(ax=ax, alpha=a, edgecolor="w", kind="bar")

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

x = [0,1,2,3,4,5,6]
y = values
colorline(x,y)

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

# Or this, maybe
#plt.title("Left", loc='left')

# Set x axis label location
ax.xaxis.set_label_position('bottom')
xlab = "Word"
ax.set_xlabel(xlab, fontsize=20, alpha=a, ha='left')
ax.xaxis.set_label_coords(-.05, -0.05)

# Customize x tick lables
xticks = labels
ax.set_xticklabels(xticks, fontsize=16, alpha=a, rotation=45)

# Customize y tick lables:
# yticks = [1,2,3,4] #etc

#plt.savefig("test.png", bbox_inches = "tight", dpi=300)
plt.show()
