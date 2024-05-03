import pandas as pd

def get_data(name):
    monsters = pd.read_csv(name, sep=',')
    return monsters

pd.set_option('display.max_columns', None)
monsters = get_data('5e_monster_data_5eTools.csv')

# Assuming 'monsters' is your DataFrame
agg_data = monsters.groupby(['cr', 'ac']).size().reset_index(name='count')

from bokeh.models import LinearColorMapper, ColorBar
from bokeh.transform import transform

# Define a color palette
palette = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", "#b3d2e9", "#9ecae1", "#85bcdb", "#6baed6", "#57a0ce", "#4292c6", "#3082be", "#2171b5", "#08519c", "#08306b"]

# Reverse the palette so higher counts are darker
palette = palette[::-1]

# Create the color mapper
mapper = LinearColorMapper(palette=palette, low=agg_data['count'].min(), high=agg_data['count'].max())

from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource

# Convert aggregated data to a ColumnDataSource
source = ColumnDataSource(agg_data)

# Create the figure
p = figure(title="AC by CR Heatmap", x_range=agg_data['cr'].unique().astype(str), y_range=agg_data['ac'].unique().astype(str),
           x_axis_label='Challenge Rating (CR)', y_axis_label='Armor Class (AC)',
           toolbar_location=None, tools="", width=800, height=800)

# Draw the rectangles
p.rect(x="cr", y="ac", width=1, height=1, source=source,
       fill_color=transform('count', mapper), line_color=None)

# Add a color bar
color_bar = ColorBar(color_mapper=mapper, location=(0, 0))
p.add_layout(color_bar, 'right')

# Display the plot
# output_file("heatmap.html")
show(p)

