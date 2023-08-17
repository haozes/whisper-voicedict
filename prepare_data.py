# Author: JhWang
# 生成语料库的json文件
import argparse
import json
import os
import functools

import soundfile
from tqdm import tqdm

from utils.utils import download, unpack
from utils.utils import add_arguments, print_arguments

def main():
    annotation_path = "dataset/"
    

    # 训练集
    data_types = ['train','test']
    
    for type in data_types:
        lines = []
        audio_dir = os.path.join("dataset/", type)
        f_json = open(os.path.join(annotation_path, type + '.json'), 'w', encoding='utf-8')
        for subfolder, _, filelist in sorted(os.walk(audio_dir)):
            for fname in filelist:
                fileName, extension = os.path.splitext(fname)
                if extension is '.wav':
                    print(fileName + "" + extension)
                    audio_path = os.path.join(subfolder, fileName + ".wav")
                    text_path = os.path.join(subfolder, fileName + ".txt")
                    if os.path.exists(text_path) and os.path.exists(audio_path):
                        with open(text_path, 'r', encoding='utf-8') as f:
                            text = f.read()
                        sample, sr = soundfile.read(audio_path)
                        duration = round(sample.shape[-1] / float(sr), 2)
                        line = {"audio": {"path": audio_path}, "sentence": text,"duration":duration}
                        print(line)
                        lines.append(line)
        for line in lines:
            f_json.write(json.dumps(line,  ensure_ascii=False)+"\n")

    pass

if __name__ == '__main__':
    main()
