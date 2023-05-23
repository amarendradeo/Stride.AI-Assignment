import spacy
import json

# Load the document into spaCy
nlp = spacy.load("en_core_web_sm")

# Identify named entities in the document
doc = nlp("The PM of the India visited the Delhi today at 1:52PM. The year is 2023 and the current unemployment rate is 4.2%.")

# Save the named entities in a JSON file
entities = [(ent.text, ent.label_) for ent in doc.ents]

with open("entities.json", "w") as f:
    json.dump(entities, f, indent=2)
