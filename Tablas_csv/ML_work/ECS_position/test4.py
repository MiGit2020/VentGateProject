#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 00:08:28 2023

concatenar dos lista

@author: pcandia
"""


import pandas as pd

wsp=['2','0','0','4.1','0','0','0','6','0','0','0','8']
wsp2= ['1','2','3','4','5','6','7','8','9','10','11','12']


wf = [float(x) for x in wsp]
wf2= [float(s) for s in wsp2]

print(wf)
print(wf2)


d = {'wsp2':wf2,'wsp':wf}
df = pd.DataFrame(d)
print(df)
