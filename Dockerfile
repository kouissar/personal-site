FROM python:3.9-slim
WORKDIR /personal-site
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
COPY . /personal-site
ENTRYPOINT ["streamlit", "run", "personal_page_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
# CMD ["app.py"]