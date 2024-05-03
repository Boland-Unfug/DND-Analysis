import pandas as pd
import numpy as np
import bokeh as bk

def get_data(name):
    monsters = pd.read_csv(name, sep=',')
    return monsters

pd.set_option('display.max_columns', None)
monsters = get_data('5e_monster_data_5eTools.csv')

players = pd.read_csv('Player_to_hit_modifiers.csv')


#take a slice of the monsters that leaves the cr and ac

print(monsters.shape)

monsters = monsters[['cr', 'ac', 'hp']]

# convert the data to numeric without seperating

monsters = monsters.apply(pd.to_numeric, errors='coerce')

players = players.apply(pd.to_numeric, errors='coerce')

# drop the rows with CR lower than 1 and higher than 20, and drop the rows with missing values

monsters = monsters[(monsters['cr'] >= 1) & (monsters['cr'] <= 20)]

monsters = monsters.dropna()

# the best regression is a 1 degree polynomial. Now lets take the average of the AC for each cr

monsters = monsters.groupby('cr').mean()

print(monsters)

# now we can plot the ac and CR

from bokeh.plotting import figure, show
from bokeh.models import HoverTool

p = figure(title='AC vs CR', x_axis_label='CR', y_axis_label='AC')

source = bk.models.ColumnDataSource(monsters)

p.line(x='cr', y='ac', source=source)

hover = HoverTool()
hover.tooltips = [
    ('CR', '@cr'),
    ('AC', '@ac')
]

p.add_tools(hover)

show(p)

# now plot the player to hits

players = players.groupby('level').mean()

p = figure(title='Player to Hit vs Level', x_axis_label='Level', y_axis_label='Player to Hit')

source = bk.models.ColumnDataSource(players)

p.line(x='level', y='modifier', source=source)

hover = HoverTool()

hover.tooltips = [
    ('Level', '@level'),
    ('To Hit', '@modifier')
]

p.add_tools(hover)

show(p)

# now we can plot the statistics of hitting a monster, correlate the CR with the to hit

# we can use the formula: (21 - AC - modifier) / 20, * 100 to get the percentage of hitting the monster

data['to_hit'] = (21 - (monsters['ac'] - players['modifier'])) / 20 * 100

p = figure(title='CR vs To Hit', x_axis_label='CR', y_axis_label='To Hit')

source = bk.models.ColumnDataSource(monsters)

p.line(x='cr', y='to_hit', source=source)

hover = HoverTool()

hover.tooltips = [
    ('CR', '@cr'),
    ('To Hit', '@to_hit')
]

p.add_tools(hover)

show(p)

# now use regression to find the best fit line

from sklearn.linear_model import LinearRegression

print(monsters.columns)

X = monsters['cr'].values.reshape(-1, 1)
y = monsters['to_hit'].values

reg = LinearRegression().fit(X, y)

print(reg.score(X, y))

print(reg.coef_)

print(reg.intercept_)

p = figure(title='CR vs To Hit', x_axis_label='CR', y_axis_label='To Hit')

source = bk.models.ColumnDataSource(monsters)

p.line(x='cr', y='to_hit', source=source)

X = np.linspace(1, 20, 100).reshape(-1, 1)

y = reg.predict(X)

p.line(X.flatten(), y, color='red')

hover = HoverTool()

hover.tooltips = [
    ('CR', '@cr'),
    ('To Hit', '@to_hit')
]

p.add_tools(hover)

show(p)