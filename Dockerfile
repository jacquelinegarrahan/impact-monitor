FROM continuumio/miniconda3

COPY environment.yml /app/environment.yml
COPY startup.py /app/startup.py
COPY monitor.py /app/monitor.py
COPY startup.sh /app/startup.sh


RUN  . /opt/conda/etc/profile.d/conda.sh &&\ 
    conda env create -f /app/environment.yml && \
    conda activate impact-monitor && \
    chmod +x /app/startup.sh

CMD ./app/startup.sh