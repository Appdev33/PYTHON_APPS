#base image
FROM python:3

RUN pip install requests
RUN pip install git+git://github.com/broadinstitute/cromwell-tools.git@v0.3.1



ADD Assign1.py ./Assign1.py
CMD ["./Assign1.py"]
ENTRYPOINT ["python"]
