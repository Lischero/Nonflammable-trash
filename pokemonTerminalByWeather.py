# -*- coding:utf-8 -*-
import os
import subprocess
import shlex
import urllib.request
import json

if __name__ == "__main__":
    api_key = os.environ.get('WEATHERAPPID')
    area_name = os.environ.get('WEATHERPLACE')
    url = "http://api.openweathermap.org/data/2.5/forecast?"+"q="+area_name+"&units=metric"+"&appid="+api_key
    source = urllib.request.urlopen(url)
    data = json.loads(source.read())
    num = data['list'][2]['weather'][0]['id']
    if num/100 == 8:
        if num%100:
            cmd = "pokemon castform" #cloud
        else:
            cmd = "pokemon castform-sun" #clear
    elif num/100 == 6:
        cmd = "pokemon castform-hail" #snow
    elif num/100 == 5 or num/100 == 3:
        cmd = "pokemon castform-rain" #rain or drizzle
    elif num/100 == 2:
        cmd = "pokemon Zapdos" #thunderstorm
    else:
        cmd = "pokemon cast-form" #other
    cmd = shlex.split(cmd)
    ret = subprocess.check_output(cmd)
    print(ret)
