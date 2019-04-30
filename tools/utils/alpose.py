from pathlib import Path
import json


def json_pack(snippets_dir, frame_width, frame_height, label='unknown', label_index=-1):
    sequence_info = []
    d_path = snippets_dir
    d_path += '/sep-json'
    p = Path(d_path)
    for path1 in sorted(p.glob('*.json')):
        path2 = path1.stem
        s_id = int(path2)
        break
    for path in sorted(p.glob('*.json')):
        json_path = str(path)
        #        print(path)
        frame_id = int(path.stem)
        if frame_id != 0 and s_id == frame_id:
            for i in range(frame_id):
                frame_data = {'frame_index': i + 1}
                skeletons = []
                frame_data['skeleton'] = skeletons
                sequence_info += [frame_data]
        frame_data = {'frame_index': frame_id + 1}
        data = json.load(open(json_path))
        skeletons = []
        for person in data['people']:
            score, coordinates = [], []
            skeleton = {}
            keypoints = person['pose_keypoints_2d']
            for i in range(0, len(keypoints), 3):
                coordinates += [round(keypoints[i] / frame_width, 3), round(keypoints[i + 1] / frame_height, 3)]
                score += [round(keypoints[i + 2], 3)]
            skeleton['pose'] = coordinates
            skeleton['score'] = score
            skeletons += [skeleton]
        frame_data['skeleton'] = skeletons
        sequence_info += [frame_data]

    video_info = dict()
    video_info['data'] = sequence_info
    video_info['label'] = label
    video_info['label_index'] = label_index

    return video_info
