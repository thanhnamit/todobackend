FROM nnguyen2/todobackend-base:latest
LABEL author="nam nguyen"
LABEL author_email="thanhnam.it@gmail.com"

COPY target /wheelhouse

RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse todobackend && \
    rm -rf /wheelhouse