import os
from pathlib import Path

data_path ='/media/a286/Elements/st-gcn/kinetics-skeleton/kinetics_val'
#data_path = '/media/a286/Elements/st-gcn/kinetics-skeleton/z/'

p = Path(data_path)
for l_path in sorted(p.glob('*')):
    l_name = l_path.stem
    l_name = str(l_name)
    if ' ' in l_name:
        r_name = l_name.replace(' ','_')
        r_path = data_path +'/'+ r_name
        l_path.rename(str(r_path))

