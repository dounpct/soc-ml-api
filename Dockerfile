FROM python:3.9

RUN pip install mlflow==2.1.1 google-cloud-storage virtualenv
# RUN pip3 install -r requirements.txt
ENV MODEL_URI ${MODEL_URI}
ENV SERVING_PORT ${SERVING_PORT}

ENV HOME="/root"
WORKDIR ${HOME}
RUN apt-get install -y git
RUN git clone --depth=1 https://github.com/pyenv/pyenv.git .pyenv
ENV PYENV_ROOT="${HOME}/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${PATH}"

COPY serving.sh /serving.sh

CMD [ "/bin/bash", "/serving.sh" ]
# CMD [ "sh", "-c", "mlflow models serve --model-uri $MODEL_URI -h 0.0.0.0 -p $SERVING_PORT"]