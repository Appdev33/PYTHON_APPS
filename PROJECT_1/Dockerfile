#base image
FROM python:3

RUN pip install requests
RUN pip install git+git://github.com/broadinstitute/cromwell-tools.git@v0.3.1



ADD Assign.py ./Assign.py
CMD ["./Assign.py"]
ENTRYPOINT ["python"]