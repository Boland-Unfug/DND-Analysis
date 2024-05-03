import Monster_analysis as ma
import Player_analysis as pa
import Attack_analysis as aa
import Analysis_Tools as at

# monster AC vs CR
monster_data = at.get_data('5e_monster_data_5eTools.csv')
monster_data = ma.clean_monster_data(monster_data)
ma.plot_ac_vs_cr(monster_data)

# player to hit vs level
player_data = at.get_data('Player_data.csv')
player_data = pa.clean_player_data(player_data)
pa.plot_player_hit_modifiers(player_data)

# to hit with cr vs level
monster_data = at.get_data('5e_monster_data_5eTools.csv')
monster_data = ma.clean_monster_data(monster_data)
player_data = at.get_data('Player_data.csv')
player_data = pa.clean_player_data(player_data)

to_hit_data = aa.find_to_hit(monster_data, player_data)
aa.plot_to_hit(to_hit_data)

# damage per round vs level

dpr_data = aa.find_dpr(monster_data, player_data)
aa.plot_dpr(dpr_data)