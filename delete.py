import os
from pathlib import Path

data_path ='/media/a286/Elements/st-gcn/kinetics-skeleton/kinetics_train'
#data_path = '/media/a286/Elements/st-gcn/kinetics-skeleton/z/'

p = Path(data_path)
for l_path in sorted(p.glob('*')):
    l_name = l_path.stem
    l_name = str(l_name)
    if 'train' in l_name:
        r_name = l_name.replace('train','')
        r_path = data_path + '/'+r_name
        l_path.rename(str(r_path))

