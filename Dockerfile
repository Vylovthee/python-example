FROM python:2.7
WORKDIR /usr/local/python-example
COPY . /usr/local/python-example
RUN pip install -i http://nexus.daocloud.io/repository/daocloud-pypi/simple  --trusted-host nexus.daocloud.io -r requirements.txt
#RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "run.py"]
