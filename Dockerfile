FROM frolvlad/alpine-python3

MAINTAINER Haioken

# set version label
ARG BUILD_DATE=2018-01-25
ARG VERSION=1.0
ARG HTTPPORT=9090
ARG PORTS='$HTTPPORT'

LABEL build_version="Haioken version:- ${VERSION} Build-date:- ${BUILD_DATE}"

# add local files, set custom NGINX directory
COPY root /
COPY approot /approot

RUN apk update \
    && apk --no-cache add iptables supervisor
    
# ports and volumes
VOLUME /config

#CMD ["/usr/bin/supervisord", "-c", "/config/supervisord.conf"]
CMD ["/usr/bin/python3", "/approot/watcher.py", "-c", "/config/watcher.cfg"]
