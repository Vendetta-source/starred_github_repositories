FROM python:3.9.8-slim

WORKDIR /github_stars_issues

ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

LABEL project='github_issues_starred' version=1.0

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

