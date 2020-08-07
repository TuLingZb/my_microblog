FROM ubuntu:trusty

MAINTAINER 17764563720@163.com

RUN ls /etc/apt
ADD sources.list /etc/apt/
RUN apt-get update \
RUN apt-get install gcc -y\
RUN apt-get install g++ -y\
RUN apt-get install gdb -y\
RUN apt-get install python-software-properties -y\
RUN apt-get install software-properties-common -y\
RUN add-apt-repository ppa:jonathonf/python-3.6 -y\
RUN apt-get update\
RUN apt-get install python3.6 -y\
RUN rm /usr/bin/python\
RUN ln -s /usr/bin/python3.6 /usr/bin/python\
RUN rm /usr/bin/python3\
RUN ln -s /usr/bin/python3.6 /usr/bin/python3\
RUN apt-get install python3-pip -y\
RUN pip3 install pip -U\
RUN rm /usr/bin/pip3 \
RUN ln -s -f /usr/local/bin/pip3 /usr/bin/pip3\
RUN ln -s -f /usr/local/bin/pip3 /usr/bin/pip\
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple


# 配置默认放置 App 的目录
RUN mkdir -p /app
WORKDIR /app
EXPOSE 80
CMD ["bash"]