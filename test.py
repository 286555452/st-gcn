import json
from pathlib import Path


d_path = '/media/a286/Elements/st-gcn/kinetics-skeleton/z/snippets/3K0Sw7rbzPU/sep-json'
p = Path(d_path)
j_name = []
for path in sorted(p.glob('*.json')):
    json_path = str(path)
    #        print(path)
    frame_id = int(path.stem)
    j_name.append(frame_id)
    #j_name += [frame_id]

    j_max = max(j_name)
    j_max = int(j_max)
for i in range(j_max):
        if i in j_name:
            print(i)