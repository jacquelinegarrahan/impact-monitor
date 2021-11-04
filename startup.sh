#!/bin/sh

. /opt/conda/etc/profile.d/conda.sh
conda activate impact-monitor
sleep 30
import-docs
sleep 30
start-monitor