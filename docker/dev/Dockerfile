FROM nnguyen2/todobackend-base:latest
LABEL author="nam nguyen"
LABEL author_email="thanhnam.it@gmail.com"

# Install dev/build dependencies
RUN apt-get update && \
    apt-get install -qy gcc python3-dev default-libmysqlclient-dev && \
    apt-get install -qy build-essential libssl-dev

# Activate virtual environment and install wheel support for packaging
RUN . /appenv/bin/activate && \
    pip install wheel --upgrade

# PIP environment variables (NOTE: must be set after installing wheel)
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache


# OUTPUT: Build artefacts (Wheels) are output here
VOLUME /wheelhouse

# OUTPUT: Build cache
VOLUME /build

# OUTPUT: Test reports are output here
VOLUME /reports

# Entrypoints
COPY docker/dev/scripts/test.sh /usr/local/bin/test.sh 
RUN chmod +x /usr/local/bin/test.sh

ENTRYPOINT [ "test.sh" ]
CMD [ "python", "manage.py", "test", "--noinput" ]

# Add application source
COPY src /application
WORKDIR /application