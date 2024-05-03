Ok, here is what I want. I want a comprehensive program that produces an impact score for each level.

It will take several things in to account:
For now: Damage, and to hit chance.

How to achieve the first part of this? time to ask some questions.
1.) make simple functions for my math
in the future:
Damage (take the average)
Damage  type (subtract likelyhood of resistance)
Range, area (range will be a small multiplier for every 30? Feet, area will be based on a maximum, and a reasonable damage.)
Nova (make damage less impactful as rounds continue)
To hit/saving throw
Bonus effects? Will determine later.
Also incorporate a skill issue (how much of the damage is based on skill)
Also incorporate extra costs for spells, such as level, or material components.

Key effects to include:
advantage/disadvantage X
Heavy weapon master / sharpshooter feats X
Critical hits X
DPR X


as for getting the data, I have a spell dataset thats pretty good, and they provide the text of the spell.
so I can do some extraction by searching for damage types and then taking a number from the text before it.
Things to remember: