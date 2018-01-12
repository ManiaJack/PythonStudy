#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'Gif倒放'

__author__ = 'ManiaJack'


def gif2fig(path):
    import os
    from PIL import Image, ImageSequence
    path = path.strip('"')
    # 获取文件绝对路径和文件名
    dir_path = os.path.split(path)[0]
    imag_name = os.path.split(path)[1]
    # 打开文件
    im = Image.open(path)
    imgs = [frame.copy() for frame in ImageSequence.Iterator(im)]
    # 反转并生成新的gif文件
    imgs.reverse()
    imgs[0].save(os.path.join(dir_path, 'reverse%s' % imag_name), save_all=True, append_images=imgs[1:])


if __name__ == '__main__':
    gif2fig(input('请输入gif文件的绝对路径：'))
    print('逆转完成。')
    __import__('time').sleep(5)
