import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

# https://python-graph-gallery.com/220-sankey-diagram-with-matplotlib/
# basic sankey chart
# The Matplotlib library has a module that allows to make basic Sankey Diagrams.
Sankey(
    flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
    labels=['', '', '', 'First', 'Second', 'Third', 'Fourth', 'Fifth'],
    orientations=[-1, 1, 0, 1, 1, 1, 0,-1])\
    .finish()
plt.title("Sankey diagram with default settings")
plt.show()