# Import necessary libraries
import pytesseract
from PIL import Image
import re
from transformers import pipeline
import sqlalchemy
import glob  # Used for file pattern matching

# Define function to convert images to text using Tesseract
def image_to_text(image_path):
    # Open an image file using the PIL library
    image = Image.open(image_path)
    # Use pytesseract to convert the image into a string of text
    return pytesseract.image_to_string(image)

# Define function to extract named entities using a BERT model
def extract_entities(text):
    # Initialize a Named Entity Recognition (NER) pipeline with a specific pre-trained model
    nlp = pipeline('ner', model='dbmdz/bert-large-cased-finetuned-conll03-english', framework='pt')
    # Process the text through the NER model to identify entities
    entities = nlp(text)
    events = []
    dates = []
    # Iterate through identified entities and categorize them as events or dates based on their entity type
    for entity in entities:
        if entity['entity'] == 'B-LOC' or entity['entity'] == 'I-LOC':
            events.append(entity['word'])
        elif entity['entity'] == 'B-DATE' or entity['entity'] == 'I-DATE':
            dates.append(entity['word'])
    return events, dates

# Define function to generate SQL commands for inserting events and dates into a database
def generate_sql_commands(events, dates):
    sql_commands = []
    # Create SQL commands to insert each event and its corresponding date into the database
    for event, date in zip(events, dates):
        sql = f"INSERT INTO events (event_name, date, time, event_duration, comments) VALUES ('{event}', '{date}', NULL, NULL, '');"
        sql_commands.append(sql)
    return sql_commands

# Define the main function that processes each image and inserts extracted data into the database
def main(image_paths):
    for image_path in image_paths:
        text = image_to_text(image_path)
        events, dates = extract_entities(text)
        sql_commands = generate_sql_commands(events, dates)
        # Connect to MySQL database using SQLAlchemy with appropriate credentials and execute SQL commands
        engine = sqlalchemy.create_engine('mysql+mysqlconnector://teamAdmin:NookBrosGotchu@mysql-db/panoptesdb')
        with engine.connect() as connection:
            for sql_command in sql_commands:
                result = connection.execute(sql_command)
                print(f"Executed: {sql_command}")

# Entry point of the script
if __name__ == "__main__":
    # Use glob to find all JPEG images in the /app directory
    image_paths = glob.glob('/app/*.jpg')
    # Execute the main function with the paths of found images
    main(image_paths)
