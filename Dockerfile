FROM python:3.9

WORKDIR /home/marvin

COPY ./requirements.txt ./requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy repo folder to working directory
COPY ./ ./

CMD python src/main.py