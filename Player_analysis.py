import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool


# Clean data
def clean_player_data(players):
    players = players.apply(pd.to_numeric, errors='coerce') # TODO will improve this so that it only targets numeric columns
    players = players.dropna()
    return players

def plot_player_hit_modifiers(players): # TODO add tooltips
    p = figure(title='Player To Hit', x_axis_label='Level', y_axis_label='To Hit Modifiers')
    source = ColumnDataSource(players)
    p.line(x='level', y='modifier', source=source)
    show(p)

def plot_player_damage(players): # TODO add tooltips
    p = figure(title='Player Damage', x_axis_label='Level', y_axis_label='Damage')
    source = ColumnDataSource(players)
    p.line(x='level', y='low_damage', source=source)
    p.line(x='level', y='high_damage', source=source)
    show(p)

