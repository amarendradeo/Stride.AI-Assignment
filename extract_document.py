import spacy

# Load the document into spaCy
nlp = spacy.load("en_core_web_sm")

# Identify headings and footers in the document
doc = nlp("Customer Loyalty Program\n\nCustomer Name: John Doe\nCustomer Address: 123 Main Street, Anytown, CA 91234\n\nFooter: https://www.sec.gov/Archives/edgar/data/27904/000002790421000003/dal-20201231.htm")

# Save the headings and footers in a JSON file
headings = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "HEADING"]
footers = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "FOOTER"]

with open("headings_and_footers.json", "w") as f:
    json.dump({"headings": headings, "footers": footers}, f, indent=2)