'''
Created on 2014-02-23

@author: Nich
'''
class Materials():
    pass

materials = Materials
materials.stone = 0
materials.crystal = 1
materials.wood = 2

materials.items = [None]*10

materials.items[materials.stone] = {'name':'stone', 'description':'stone'}
materials.items[materials.crystal] = {'name':'crystal', 'description':'crystal'}
materials.items[materials.wood] = {'name':'wood', 'description':'wood'}
        
        

        