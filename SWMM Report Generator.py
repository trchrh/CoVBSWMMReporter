"""
Creating a SWMM report from the .inp and .rpt file
"""

class py_Subcatchment:
    def __init__(self, name, outlet, area, width,
                 perc_slope, n_perv, n_imp, perc_routed, suction,
                 hydcon, imdmax, discharge):
        self.name = name
        self.outlet = outlet
        self.area = area
        self.width = width
        self.perc_slope = perc_slope
        self.n_perv = n_perv
        self.n_imp = n_imp
        self.perc_routed = perc_routed
        self.suction = suction
        self.hydcon = hydcon
        self.imdmax = imdmax
        self.discharge = -1
    

inp = []
subcatchments = []
subareas = []
infiltration = []
junctions = []
outfalls = []
storagenodes = []
conduits = []
weirs = []
#strips all comment lines from .inp file
with open('100yr.inp', "r") as f:
    lines = f.readlines()
    for line in lines:
        if ";" in line:
            pass
        else:
            inp.append(line.strip("\n"))
            
#create iterable ranges based in .inp sections            
subcat_range = inp.index('[SUBAREAS]') - inp.index('[SUBCATCHMENTS]')
subareas_range = inp.index('[INFILTRATION]') - inp.index('[SUBAREAS]')
infiltration_range = inp.index('[JUNCTIONS]') - inp.index('[INFILTRATION]')
junctions_range = inp.index('[OUTFALLS]') - inp.index('[JUNCTIONS]')
outfalls_range = inp.index('[STORAGE]') - inp.index('[OUTFALLS]')
storagenodes_range = inp.index('[CONDUITS]') - inp.index('[STORAGE]')
conduits_index = inp.index('[WEIRS]') - inp.index('[CONDUITS]')
weirs_index = inp.index('[XSECTIONS]') - inp.index('[WEIRS]')

#break the file into sections
for i in range(1, subcat_range):  
    line = inp[i+inp.index('[SUBCATCHMENTS]')]
#     print(line)
#     print('~~~')
    if line != "":
        name = line.split()[0]
        outlet = line.split()[2]
        area = float(line.split()[3])
        perc_slope = float(line.split()[6])
        width = float(line.split()[5])
        
        subcatchments.append([name, outlet, area, perc_slope, width])

for i in range(1, subareas_range):  
    line = inp[i+inp.index('[SUBAREAS]')]
    if line != "":
        n_imp = float(line.split()[1])
        n_perv = float(line.split()[2])
        perc_routed = float(line.split()[7])

        subareas.append([n_imp, n_perv, perc_routed])
        
for i in range(1, infiltration_range):  
    line = inp[i+inp.index('[INFILTRATION]')]
    if line != "":
        suction = float(line.split()[1])
        hydcon = float(line.split()[2])
        imdmax = float(line.split()[3])

        infiltration.append([suction, hydcon, imdmax])
        
for i in range(1, junctions_range):  
    line = inp[i+inp.index('[JUNCTIONS]')]
    if line != "":
        name = line.split()[0]
        invert_ele = float(line.split()[1])
        maxdepth_allowable = float(line.split()[2])
        init_depth = float(line.split()[3])

        junctions.append([name, invert_ele, maxdepth_allowable, init_depth])
    


#create object from .rpt file
#break the .rpt file into sections

#create output fille
#create a subcatchment section

#select input object and go to subcatchments

#loop through the .inp file subcatchment section,
#record the outlet, area, percent impervious, width, & % slope
#use the subcatchment name to search the infiltration section for the suction
#head, hydcon, and IMDmax
#search .rpt file and grab peak discharge
#record the subcatchment values into the output file.

#create a junctions section

#Loop through the junction section of the .inp file and record the name.
#grab the inv ele, max depth, init depth
#search the .rpt file and get the maximum depth depth**, HGL, and Qin.
#record the junction into the output file

#create an outfalls section

#Loop through and grab the name and invert elevation.
#search the .rpt file and get the HGL and q max

#create a storage section

#loop through and get each name, invert elevation, 
#get qin and max HGL

#create a conduits section

#loop through and get each name, inlet node, outlet node, length, n
#inlet offset, outlet offset
#get max flow, d/D ratio and velocity

#create a weir section
#get weird name, inlet node, outlet node, weird type, crest height, coe, and discharge

