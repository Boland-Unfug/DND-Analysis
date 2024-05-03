import pandas as pd
import Analysis_Tools as at
import Damage_Calculations as dc
import Monster_analysis as ma
import Player_analysis as pa
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool

# make a new dataset for the new calculations

def find_to_hit(monster_data, player_data):
    monster_data = monster_data[['cr','ac']]
    monster_means = ma.group_monster_data(monster_data, 'cr')
    to_hit_data = pd.DataFrame()
    to_hit_data['cr'] = monster_means['cr']
    monster_means = monster_means['ac']
    player_data = player_data['modifier']
    to_hit_data['to_hit'] = dc.calculate_to_hit(monster_means, player_data)
    return to_hit_data

def find_dpr(monster_data, player_data):
    to_hit_data = find_to_hit(monster_data, player_data)
    print(to_hit_data)
    dpr_data = pd.DataFrame()
    dpr_data['cr'] = to_hit_data['cr']

    dpr_data['low_dpr'] = dc.calculate_dpr(to_hit_data['to_hit'], player_data['low_damage'])
    dpr_data['high_dpr'] = dc.calculate_dpr(to_hit_data['to_hit'], player_data['high_damage'])
    return dpr_data


def plot_to_hit(to_hit_data): #TODO add tooltips
    p = figure(title='To Hit vs CR', x_axis_label='CR', y_axis_label='To Hit')
    source = ColumnDataSource(to_hit_data)
    p.line(x='cr', y='to_hit', source=source)
    show(p)

def plot_dpr(dpr_data): #TODO add tooltips
    p = figure(title='DPR vs CR', x_axis_label='CR', y_axis_label='DPR')
    source = ColumnDataSource(dpr_data)
    p.line(x='cr', y='low_dpr', source=source, color='red', legend_label='Low DPR')
    p.line(x='cr', y='high_dpr', source=source, color='blue', legend_label='High DPR')
    show(p)