import os
import base64
from . import AutoXuexiPlaywrightCore

APPID="AutoXuexiPlaywright"
APPICON="""iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAADeUlEQVRIie2WbWhWZRjH/5vnCaIPQSNMocYTjD70MjWWYumYQ2tiG1YoSkzLaVRQiLZyFUQfil6s5UgGg4Fk
        hhiuxd7SvTrcRDcjpfq4F9CtfGboBN15nnN+fbjceXp8XiYY2YfdcOBwn+u6fv/7uq/7uk+WK6HbMLJvB3QWPAtOGKFz5+X81+DQxs2S78m7BdCcG2GuRKaHkrXgurBhE66Er7t
        hxZqMPgn+9y+Awz9AXz8MDQXzGcF8uhvG/zCnsvU2d/IUXLtG7AbbqATlFXgSMQnK1kNPL7S24SsLStdB/4nMYFaVQfGzxCQ8Cc6dh+XP2Lf6fbDn67htQRHU1sHoKABoPigH3t
        gBeQXXs3QHjI2DctKDfTmQuxAmJ6FoNeyuhj8vwJmzoAfhyhW8BHvB4hWwcDn8csbEPPYkaH5cXGc3vLglgZME5pPPLU1ffGWrvRABz7PVRCZg1/sJ4MBvxzvw3gf2/uZOuHTZ0
        l+6Dhoak+yTwW/tgsHT9t7aBnkF4OTFBVz8C1zX9rGyCrqPmcCfjgappaExEMfAYEqhKVItqK3Dnd7f5zdCRxd8/Blsfc3Aq8osaHmFiQk/DpOTRKeLLBaDRYWw+rkgCzOCg5UX
        lkBXD2x73YK99AoMDcGS4rjN3lrYsAkeWQqjo/F5zbOMHGkHzUsZP6mBOHIU+v6wtGyxvKJCqfW4nKZmKZwrLxxW9ERH3Dj3AWlRvnSyXYpMyJEUKq9QVGN2yS/IV1RjqTtKUAx
        LV8LmbVaB11XS1GxF9Y+DH6zqvkftCJ0asMx09VgcsC1SGLqPpe0RBu7rt32prEr46El2Hn/7HVpaoaeX6DR4STGMjIDutXO7shSmpuDtd20BV69C25EZwL4P7Z3JnWjZ09apXB
        e++RbWvJAyiCfB8DBsrzSB1TVW8fsPzACu3xfvTPlPwdEOU3zpsjWSkrVpA0QlaG6BL/fAxEU4eMji7D+Q1DQyVnVMgrp62PKqBT39cyAqZfXX7IWch2FgEHqPQ3OLzY+N46fxc
        SWSrlhfUvbWl+VJN/f7OTUldX4nNTZJjiOvqlKhg4ekSESxDG4p73ZfklNdI+XcI82dK911Z9oA/s7tyo7FpOER6eyvmpNXIPm+1PBjZsHpUuFKdln09cNDT6S1cSX48KOU/TjT
        k+XeZEb/7fH//9mbBd/q+BuapkzTsaP4XQAAAABJRU5ErkJggg=="""
APPICONBYTES=base64.b64decode(APPICON)

def start_core():
    os.chdir(os.path.join(os.path.split(os.path.realpath(__file__))[0],".."))
    # 将工作目录转移到脚本所在目录的上层目录，保证下面的相对路径都能正确找到文件以及符合修改后的项目结构
    processor=AutoXuexiPlaywrightCore.XuexiProcessor()
    processor.start()