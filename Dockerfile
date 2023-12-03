FROM jupyter/minimal-notebook:notebook-7.0.6

WORKDIR /home/jovyan

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt