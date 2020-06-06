FROM centos:7
RUN yum -y groups mark install "Development Tools" > /tmp/foo.txt && \
    yum -y groups mark convert "Development Tools" > /tmp/foo.txt && \
    yum -y groupinstall "Development Tools" > /tmp/foo.txt && \
    yum -y groupinstall "Development Tools" > /tmp/foo.txt && \
        yum -y install openssl-devel bzip2-devel libffi-devel > /tmp/foo.txt && \
        yum -y install wget > /tmp/foo.txt && \
        yum -y install git > /tmp/foo.txt

ENV PYTHON_URL https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
RUN wget $PYTHON_URL > /tmp/foo.txt && tar xvf Python-3.8.3.tgz > /tmp/foo.txt
RUN cd Python-3.8*/ && \
        ./configure --enable-optimizations > /tmp/foo.txt && \
        make altinstall

ENV PATH $PATH:/usr/local/bin
CMD ["python3.8", "--version"]
CMD ["pip3.8", "--version"]

