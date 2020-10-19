# South African Lottery API Docker Image
# Creation Date: 09 Sept 2020, 00:38
# Author: Sizwe-se-Afrika Immaculate Mkhonza

# base image, linux distro os
FROM alpine:latest

# envorment keys, for:
# workdir, mongo_db 
ENV APP_PATH=$(pwd)/app
ENV APP_MONGO_DB_PATH=$APP_PATH/cluster/

# create workdir
RUN mkdir -p $APP_PATH

# define 
WORKDIR $APP_PATH

# copy all source code resources to workdir
COPY . .

# setup requirements
RUN apk add chromium
RUN ln -s /usr/bin/chromium-browser /usr/bin/google-chrome

RUN apk add --update python3
RUN python3 -m ensurepip
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -I -r requirements.txt

# expose, the api port; 5000
EXPOSE 5000 5000

# run python
ENTRYPOINT ["python3","main.py" ]
