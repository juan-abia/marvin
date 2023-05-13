FROM python:3.9

WORKDIR /home/marvin

# Copy repo folder to working directory
COPY ./ ./

# Install dependencies
RUN pip install -r requirements.txt

CMD python src/main.py