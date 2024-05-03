def calculate_to_hit(target_ac, attack_modifier):
    return (21 - (target_ac - attack_modifier))/20 * 100
    
def calculate_target_ac(hit_percentage, attack_modifier):
    return 21 - (hit_percentage / 100 * 20) + attack_modifier

def calculate_attack_modifier(hit_percentage, target_ac):
    return 21 - (target_ac - (hit_percentage / 100 * 20))

def calculate_dpr(hit_percentage, damage):
    return (hit_percentage / 100) * damage

def add_advantage(hit_percentage):
    return (hit_percentage - add_disadvantage(hit_percentage)) + hit_percentage 

def add_disadvantage(hit_percentage):
    return hit_percentage ** 2

def calculate_crit_damage(damage, crit_chance = 0.05):
    return damage + (damage * crit_chance)

def add_master(attack_modifier,target_ac, damage):
    damage += 10
    attack_modifier -= 5
    return calculate_dpr(calculate_to_hit(target_ac, attack_modifier), damage)

def add_master(hit_percentage, damage):
    damage += 10
    hit_percentage -= 25
    return calculate_dpr(hit_percentage, damage)

def use_master_threshhold(attack_modifier, damage):
    return attack_modifier - damage/2 + 16 

def should_use_master(ac, attack_modifier, damage):
    return ac < use_master_threshhold(attack_modifier, damage)

def plus_one_weapon(attack_modifier):
    return attack_modifier + 1

def plus_two_weapon(attack_modifier):
    return attack_modifier + 2

def plus_three_weapon(attack_modifier):
    return attack_modifier + 3