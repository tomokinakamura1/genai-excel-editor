FROM python:3.11
RUN apt-get update && apt-get install -y --no-install-recommends gcc
WORKDIR /application
# RUN python -m venv .venv
# RUN . .venv/bin/activate
# RUN pip install pipenv
COPY requirements.txt .
# RUN pipenv install
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "gradio-ui.py"]