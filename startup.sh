#!/bin/sh

. /opt/conda/etc/profile.d/conda.sh
conda activate impact-monitor
python /app/startup.py 
python /app/monitor.py 