import os
import argparse
import json
from pathlib import Path
import shutil

from .io import IO
import tools.utils as utils


class Pose(IO):
    """
        Demo for Skeleton-based Action Recgnition
    """

    def start(self):

        openpose = '{}/examples/openpose/openpose.bin'.format(self.arg.openpose)

        p = Path(self.arg.video)
        for path in sorted(p.glob('*.mp4')):
            video_name = path.stem
            path = str(path)
            output_snippets_dir = '{}/snippets'.format(self.arg.video)
            output_sequence_dir = '{}/data'.format(self.arg.video)
            output_sequence_path = '{}/{}.json'.format(output_sequence_dir, video_name)
#        video_name = self.arg.video.split('/')[-1].split('.')[0]

            # load label
            label_path = self.arg.label
            with open(label_path) as f:
                label_info = json.load(f)

            sample_id = ''.join(video_name)
            if not label_info[sample_id]['label']  == None:
                label = label_info[sample_id]['label']
            else :
                label = 'nothing'

            if not label_info[sample_id]['label_index'] == None:
                label_index = label_info[sample_id]['label_index']
            else:
                label_index = -1


            # pose estimation
            openpose_args = dict(
                video=path,
                write_json=output_snippets_dir,
                display=0,
                render_pose=0,
                model_pose='COCO')
            command_line = openpose + ' '
            command_line += ' '.join(['--{} {}'.format(k, v) for k, v in openpose_args.items()])
            shutil.rmtree(output_snippets_dir, ignore_errors=True)
            os.makedirs(output_snippets_dir)
            os.system(command_line)

            # pack openpose ouputs
            video = utils.video.get_video_frames(path)
            height, width, _ = video[0].shape
            video_info = utils.pose.json_pack(
                output_snippets_dir, video_name, width, height, label=label,label_index=label_index)
            if not os.path.exists(output_sequence_dir):
                os.makedirs(output_sequence_dir)
            with open(output_sequence_path, 'w') as outfile:
                json.dump(video_info, outfile)
            if len(video_info['data']) == 0:
                print('Can not find pose estimation results.')
                return
            else:
                print('%s Pose estimation complete.', video_name)


    @staticmethod
    def get_parser(add_help=False):

        # parameter priority: command line > config > default
        parent_parser = IO.get_parser(add_help=False)
        parser = argparse.ArgumentParser(
            add_help=add_help,
            parents=[parent_parser],
            description='Pose for Spatial Temporal Graph Convolution Network')

        # region arguments yapf: disable
        parser.add_argument('--video',
            default='/media/a286/Elements/st-gcn/kinetics-skeleton/z',
            help='Path to video')
        parser.add_argument('--label',
            default='/media/a286/Elements/st-gcn/kinetics-skeleton/kinetics_val_label.json',
            help='Path to label')
        parser.add_argument('--openpose',
            default='../openpose/build',
            help='Path to openpose')
        parser.add_argument('--height',
            default=1080,
            type=int,
            help='Path to save results')
        parser.set_defaults(config='./config/st_gcn/kinetics-skeleton/demo.yaml')
        parser.set_defaults(print_log=False)
        # endregion yapf: enable

        return parser