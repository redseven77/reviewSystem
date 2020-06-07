FROM centos:7
WORKDIR /usr/src
RUN yum -y groups mark install "Development Tools" && \
    yum -y groups mark convert "Development Tools" && \
    yum -y groupinstall "Development Tools" && \
    yum -y groupinstall "Development Tools" && \
    yum -y install postgresql-devel unixODBC-devel postgresql && \
    yum -y install openssl-devel bzip2-devel libffi-devel && \
    yum -y install wget && \
    yum -y install git

ENV PYTHON_URL https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
RUN wget $PYTHON_URL > /tmp/foo.txt && tar xvf Python-3.8.3.tgz
RUN cd Python-3.8*/ && \
        ./configure --enable-optimizations && \
        make altinstall
ENV PATH $PATH:/usr/local/bin
RUN ln -s /usr/local/bin/python3.8 /usr/bin/python3 && \
    ln -s /usr/local/bin/pip3.8 /usr/bin/pip3
CMD ["python3", "--version"]
CMD ["pip3", "--version"]
RUN python3 -m venv venv && \
    source venv/bin/activate

EXPOSE 8000
COPY . .
RUN pip3 install -r requirements.txt && \
    pip3 freeze
WORKDIR /usr/src/userReview
#RUN python3 manage.py migrate && \
#    python3 manage.py load_data --name foods.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]