import os
from pathlib import Path


data_path ='/media/a286/Elements/st-gcn/kinetics-skeleton/kinetics_val'
#data_path = '/media/a286/Elements/st-gcn/kinetics-skeleton/z/'
ffmpeg = 'ffmpeg'
p = Path(data_path)
for l_path in sorted(p.glob('*')):
    l_name = l_path.stem
    #if l_name[0] > 'g':
    q = Path(l_path)
    for v_path in sorted(q.glob('*.mp4')):
        v_name = v_path.stem
        v_name = str(v_name)
        v_path = str(v_path)
        ffmeg_args = dict(
            y='',
            vf='scale=340:256',
            r=30,
            strict=-2)
        ffmeg_list = ffmpeg + ' -i ' + v_path + ' '
        ffmeg_list += ' '.join(['-{} {}'.format(k, v) for k, v in ffmeg_args.items()])
        out_path = ' /media/a286/Elements/st-gcn/kinetics-skeleton/z/' + v_name + '.mp4'
        ffmeg_list += out_path
        os.system(ffmeg_list)
        q = str(q)
        mv = 'mv' + out_path + ' ' + q
        os.system(mv)






