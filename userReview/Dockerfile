FROM centos:7
WORKDIR /usr/src
RUN yum -y groups mark install "Development Tools" > /tmp/foo.txt && \
    yum -y groups mark convert "Development Tools" > /tmp/foo.txt && \
    yum -y groupinstall "Development Tools" > /tmp/foo.txt && \
    yum -y groupinstall "Development Tools" > /tmp/foo.txt && \
    yum -y install postgresql-devel unixODBC-devel postgresql && \
    yum -y install openssl-devel bzip2-devel libffi-devel > /tmp/foo.txt && \
    yum -y install wget > /tmp/foo.txt && \
    yum -y install git > /tmp/foo.txt

ENV PYTHON_URL https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
RUN wget $PYTHON_URL > /tmp/foo.txt && tar xvf Python-3.8.3.tgz > /tmp/foo.txt
RUN cd Python-3.8*/ && \
        ./configure --enable-optimizations > /tmp/foo.txt && \
        make altinstall
ENV PATH $PATH:/usr/local/bin
RUN ln -s /usr/local/bin/python3.8 /usr/bin/python3 > /tmp/foo.txt && \
    ln -s /usr/local/bin/pip3.8 /usr/bin/pip3 > /tmp/foo.txt
CMD ["python3", "--version"]
CMD ["pip3", "--version"]
RUN python3 -m venv venv && \
    source venv/bin/activate

EXPOSE 8000
COPY . .
RUN pip3 install -r requirements.txt > /tmp/foo.txt && \
    pip3 freeze
WORKDIR /usr/src/userReview
#RUN python3 manage.py migrate && \
#    python3 manage.py load_data --name foods.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]