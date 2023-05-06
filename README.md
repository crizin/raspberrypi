# Setup

```shell
git clone https://github.com/crizin/raspberrypi.git
pip install -r requirements.txt
```

# Crontab
```
* * * * * crizin python /home/crizin/rasberrypi/monitor.py > /dev/null 2>&1
```
