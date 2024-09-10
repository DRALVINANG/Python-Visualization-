#Paste this whole chunk into your Google Colab Cell:

# Create a new custom.mplstyle file and open it for writing
with open('custom.mplstyle', 'w') as f:
    f.write("""# Generic figure tweaks
figure.figsize: 10, 6  
figure.dpi: 125  
savefig.dpi: 300 
savefig.bbox: tight  
axes.prop_cycle: cycler("color", ["006ba4", "ff800e", "ababab", "595959", "5f9ed1", "c85200", "898989", "a2c8ec", "ffbc79", "cfcfcf"])
axes.spines.top: False
axes.spines.right: False


# Text
font.size: 14
font.family: sans-serif
font.sans-serif: DejaVu Sans
axes.titlesize: 20
axes.titleweight: bold
axes.titlelocation: left
axes.labelsize: large
xtick.labelsize: medium
ytick.labelsize: medium


# Legend
legend.loc: "upper right"
legend.numpoints: 3 
legend.scatterpoints: 3


# Grid
axes.grid: True
axes.axisbelow: True  
grid.color: "#d3d3d3"
grid.linestyle: : 
grid.linewidth: 1.0


# Line chart only
lines.linewidth: 3
lines.marker: o
lines.markersize: 8
""")

#----------------------------------------------------------------
import matplotlib.pyplot as plt

# Use the custom style
plt.style.use('custom.mplstyle')

# Example plot to test the style
plt.figure()
plt.plot([1, 2, 3], [1, 4, 9])
plt.title('Test Plot')
plt.show()

#From now on.. all your Python charts will look good!
