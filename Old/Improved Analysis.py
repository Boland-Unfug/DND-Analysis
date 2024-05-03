import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from Analysis_Tools import get_data, drop_sources


pd.set_option('display.max_columns', None)
monsters = get_data('5e_monster_data_5eTools.csv')

# Remove unnecessary data
monsters = drop_sources(monsters)
monsters = monsters[['cr', 'ac', 'hp', 'name']]
monster_names = monsters['name']
monsters = monsters[['cr', 'ac', 'hp']]
monsters = monsters.apply(pd.to_numeric, errors='coerce')
monsters['name'] = monster_names
monsters = monsters[(monsters['cr'] >= 1) & (monsters['cr'] <= 20)] # drop crs that are not between 1 and 20
monsters = monsters.drop_duplicates(subset='name') # drop repeating names
monsters = monsters.dropna() # drop missing values

# copy the data to a new dataset
# group the data by cr and take the mean of the ac
monster_means = monsters[['cr', 'ac']]
print(monster_means)
monster_means = monster_means.groupby('cr').mean()
monster_means = monster_means.reset_index()
print(monsters)
# make the points larger but also transparent
p = figure(title='AC vs CR', x_axis_label='CR', y_axis_label='AC')

source = ColumnDataSource(monsters)
source2 = ColumnDataSource(monster_means)

p.scatter(x='cr', y='ac', source=source, size=15, alpha=0.1, line_color="black", line_alpha=0.5)

p.line(x='cr', y='ac', source=source2, width=10, line_color="black")

tooltips1 = [
    ('Name', '@name')
]
tooltips2 = [
    ('CR', '@cr'),
    ('AC', '@ac')
]

hover1 = HoverTool(tooltips = tooltips1)
hover2 = HoverTool(tooltips = tooltips2)

p.add_tools(hover1, hover2)

show(p)

# Player To hit graph



players = get_data('Player_data.csv')

# Clean data
players = players.apply(pd.to_numeric, errors='coerce')
players = players.dropna()

# Calculate to hits
players['to_hit'] = (21 - (monster_means['ac'] - players['modifier'])) / 20 * 100

# Plot
p = figure(title='Player to Hit vs CR', x_axis_label='CR', y_axis_label='Player to Hit')

source = ColumnDataSource(players)

p.line(x='level', y='to_hit', source=source)

hover = HoverTool()
hover.tooltips = [
    ('Level', '@level'),
    ('To Hit', '@to_hit')
]

p.add_tools(hover)

show(p)

# print the average to hit for each level
print(sum(players['to_hit']) / len(players['to_hit']))

# now I need a damage per round graph that takes in to account the to hit and the damage, use low damage for now.

# I will use the formula: (to_hit / 100) * damage

players['dpr_low'] = (players['to_hit'] / 100) * players['low_damage']
players['dpr_high'] = (players['to_hit'] / 100) * players['high_damage']

p = figure(title='Player Damage per Round vs CR', x_axis_label='CR', y_axis_label='Player Damage per Round')

source = ColumnDataSource(players)

p.line(x='level', y='dpr_low', source=source)

p.line(x='level', y='dpr_high', source=source)

hover = HoverTool()

hover.tooltips = [
    ('Level', '@level'),
    ('DPR_low', '@dpr_low')
    # ('DPR_high', '@dpr_high')
]

p.add_tools(hover)

show(p)

