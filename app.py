from Bio import Entrez, SeqIO
from Bio.Entrez import efetch
from flask import Flask, render_template, request
import time

app = Flask(__name__)

Entrez.email = "noreply@example.com"

def search_sequences(organism, enzyme, sequence_type):
    try:
        search_term = f'{organism}[Organism] {enzyme}'
        db = "nucleotide" if sequence_type == "nucleotide" else "protein"
        
        handle = Entrez.esearch(db=db, term=search_term, retmax=5)
        record = Entrez.read(handle)
        handle.close()
        
        if not record["IdList"]:
            return {"error": f"No {sequence_type} sequences found for {enzyme} in {organism}"}
        
        sequence_id = record["IdList"][0]
        handle = Entrez.efetch(db=db, id=sequence_id, rettype="gb", retmode="text")
        seq_record = SeqIO.read(handle, "genbank")
        handle.close()
        
        result = {
            "ID": sequence_id,
            "Description": seq_record.description,
            "Sequence": str(seq_record.seq),
            "Length": len(seq_record.seq),
            "Annotations": seq_record.annotations,
            "Features": [],
            "Sequence_Type": sequence_type,
            "Full_Record": str(seq_record.format("genbank"))
        }
        
        start_position = None
        if sequence_type == "nucleotide":
            for feature in seq_record.features:
                feature_info = {
                    "Type": feature.type,
                    "Location": str(feature.location),
                    "Qualifiers": feature.qualifiers,
                    "Strand": str(feature.location.strand) if feature.location else "Not specified",  # Updated to .location.strand
                    "Location_Parts": [str(part) for part in feature.location.parts] if hasattr(feature.location, "parts") else [str(feature.location)]  # Handle CompoundLocation
                }
                result["Features"].append(feature_info)
                if feature.type in ["CDS", "gene"] and enzyme.lower() in str(feature.qualifiers.get("product", "")).lower():
                    start_position = feature.location.start
            result["Start_Position"] = start_position if start_position is not None else "Not specified in record"
        else:
            for feature in seq_record.features:
                feature_info = {
                    "Type": feature.type,
                    "Location": str(feature.location),
                    "Qualifiers": feature.qualifiers,
                    "Strand": str(feature.location.strand) if feature.location else "Not specified",  # Updated to .location.strand
                    "Location_Parts": [str(part) for part in feature.location.parts] if hasattr(feature.location, "parts") else [str(feature.location)]  # Handle CompoundLocation
                }
                result["Features"].append(feature_info)
        
        return result
        
    except Exception as e:
        return {"error": f"Error occurred: {str(e)}"}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        organism = request.form['organism']
        enzyme = request.form['enzyme']
        sequence_types = request.form.getlist('sequence_type')
        
        if not sequence_types:
            return render_template('index.html', error="Please select at least one sequence type")
        
        nucleotide_result = None
        protein_result = None
        
        if "nucleotide" in sequence_types:
            nucleotide_result = search_sequences(organism, enzyme, "nucleotide")
            time.sleep(1)
        if "protein" in sequence_types:
            protein_result = search_sequences(organism, enzyme, "protein")
        
        return render_template('results.html', 
                             nucleotide_result=nucleotide_result, 
                             protein_result=protein_result)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)