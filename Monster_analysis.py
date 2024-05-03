import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool
from Analysis_Tools import get_data, drop_sources


# Remove unnecessary data
def clean_monster_data(monsters):
    monsters = drop_sources(monsters)
    monsters = monsters[['cr', 'ac', 'hp', 'name']]
    monster_names = monsters['name']
    monsters = monsters[['cr', 'ac', 'hp']]
    monsters = monsters.apply(pd.to_numeric, errors='coerce')
    monsters['name'] = monster_names
    monsters = monsters[(monsters['cr'] >= 1) & (monsters['cr'] <= 20)] # drop crs that are not between 1 and 20
    monsters = monsters.drop_duplicates(subset='name') # drop repeating names
    monsters = monsters.dropna() # drop missing values
    return monsters

def ac_vs_cr(monsters):
    monsters = monsters[['cr', 'ac']]
    return monsters

def group_monster_data(monsters, flag): # TODO make this able to take a flag for which column to group by
    # take the mean of the data, grouped by the flag
    if flag.isnumeric():
        flag = str(flag)
    monster_means = monsters.groupby(flag).mean()
    monster_means = monster_means.reset_index()
    return monster_means

def plot_ac_vs_cr(monsters): # TODO fix CR tooltips
    # copy the data to a new dataset
    monsters = ac_vs_cr(monsters)
    monster_means = group_monster_data(monsters, 'cr')

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