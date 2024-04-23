import pytesseract
from PIL import Image
import re
from transformers import pipeline
import sqlalchemy

def image_to_text(image_path):
    # Open an image file using the PIL library
    image = Image.open(image_path)
    # Use pytesseract to convert the image into a string of text
    return pytesseract.image_to_string(image)

def extract_entities(text):
    # Initialize a Named Entity Recognition (NER) pipeline from the 'transformers' library
    # This particular model identifies different types of named entities in text
    nlp = pipeline('ner', model='dbmdz/bert-large-cased-finetuned-conll03-english', framework='pt')
    # Process the text through the NER model to identify entities
    entities = nlp(text)
    events = []
    dates = []

    # Loop through each identified entity
    for entity in entities:
        # If the entity is a location (used here as a proxy for 'events'), add it to the events list
        if entity['entity'] == 'B-LOC' or entity['entity'] == 'I-LOC':
            events.append(entity['word'])
        # If the entity is a date, add it to the dates list
        elif entity['entity'] == 'B-DATE' or entity['entity'] == 'I-DATE':
            dates.append(entity['word'])

    # Return lists of events and dates
    return events, dates

def generate_sql_commands(events, dates):
    sql_commands = []
    # Generate SQL commands to insert each event and its corresponding date into a database
    for event, date in zip(events, dates):
        sql = f"INSERT INTO events (event_name, date, time, event_duration, comments) VALUES ('{event}', '{date}', NULL, NULL, '');"
        sql_commands.append(sql)
    return sql_commands

def main(image_path):
    # Convert image to text
    text = image_to_text(image_path)
    # Extract events and dates from the text
    events, dates = extract_entities(text)
    # Generate SQL commands based on the extracted data
    sql_commands = generate_sql_commands(events, dates)

    # Connect to a MySQL database using SQLAlchemy and execute the SQL commands
    engine = sqlalchemy.create_engine('mysql+mysqlconnector://user:password@localhost/panoptesdb')
    with engine.connect() as connection:
        for sql_command in sql_commands:
            result = connection.execute(sql_command)
            print(f"Executed: {sql_command}")

if __name__ == "__main__":
    # Set the path to the image file
    image_path = 'path_to_your_image_or_document.jpg'
    # Call the main function with the image path
    main(image_path)
