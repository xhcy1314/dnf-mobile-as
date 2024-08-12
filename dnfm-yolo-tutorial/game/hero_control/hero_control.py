#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : huxiansheng (you@example.org)
# @Date    : 2024/8/6
from device_manager.scrcpy_adb import ScrcpyADB


def get_hero_control(name: str, scrcpy_adb: ScrcpyADB):
    """
    获取英雄控制的实例
    :param name:英雄名称
    :param scrcpy_adb:设备链接实例
    :return:
    """
    if name == 'nai_ma':
        from game.hero_control.nai_ma import NaiMa
        return NaiMa(scrcpy_adb)
    elif name == 'nan_qiang_pao':
        from game.hero_control.nan_da_qiang import NanDaQiang
        return NanDaQiang(scrcpy_adb)
    elif name == 'hong_yan':
        from game.hero_control.hong_yan import HongYan
        return HongYan(scrcpy_adb)
    elif name == 'nv_qi_gong':
        from game.hero_control.nv_qi_gong import NvQiGong
        return NvQiGong(scrcpy_adb)
    else:
        raise ValueError(f'{name} is not support')


if __name__ == '__main__':
    adb = ScrcpyADB()
    hero = get_hero_control('nai_ma', adb)
    hero.skill_combo_1()
    adb.display_frames()
