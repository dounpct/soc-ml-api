FROM python:3.9

ENV HOME="/root"
WORKDIR ${HOME}

# RUN pip install mlflow==2.1.1 google-cloud-storage pathlib==1.0.1 lz4==3.1.3 psutil==5.9.0 typing-extensions==4.3.0 cloudpickle==2.2.1
RUN pip install google-cloud-storage

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV MODEL_URI ${MODEL_URI}
ENV SERVING_PORT ${SERVING_PORT}

# RUN apt-get install -y git
# RUN git clone --depth=1 https://github.com/pyenv/pyenv.git .pyenv
# ENV PYENV_ROOT="${HOME}/.pyenv"
# ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"

COPY serving.sh /serving.sh

CMD [ "/bin/bash", "/serving.sh" ]
# CMD [ "sh", "-c", "mlflow models serve --model-uri $MODEL_URI -h 0.0.0.0 -p $SERVING_PORT --no-conda"]