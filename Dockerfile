FROM python:3
COPY . /assgn
WORKDIR /assgn
RUN pip install -r req.txt
ENTRYPOINT ["python"]
CMD ["assgn.py"]
EXPOSE 8081