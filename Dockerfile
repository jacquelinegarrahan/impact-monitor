FROM continuumio/miniconda3

COPY environment.yml /app/environment.yml
COPY . /app/impact-monitor


RUN  . /opt/conda/etc/profile.d/conda.sh &&\ 
    conda env create -f /app/environment.yml && \
    conda activate impact-monitor && \
    pip install /app/impact-monitor && \
    chmod +x /app/impact-monitor/startup.sh

CMD ./app/impact-monitor/startup.sh