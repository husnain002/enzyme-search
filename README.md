# 🧬 Enzyme Sequence Finder

![Enzyme Sequence Finder Banner](https://img.shields.io/badge/Enzyme%20Sequence%20Finder-Decode%20Enzymes%20with%20Precision-blue?style=for-the-badge&logo=flask)

**Enzyme Sequence Finder** is a Flask-powered web application that electrifies your bioinformatics research! Built with Biopython, it queries the NCBI database to retrieve nucleotide and protein sequences for specific enzymes in chosen organisms. With a sleek, DNA-inspired interface, this tool is perfect for researchers, students, and bioinformaticians eager to explore the molecular world. Unravel the secrets of enzymes with precision! 🧬

## 🌟 Features

- **🔍 Enzyme-Specific Search**: Query nucleotide and protein sequences by organism and enzyme from NCBI.
- **🧬 Dual Sequence Retrieval**: Fetch both nucleotide and protein data in one go.
- **📊 Rich Sequence Data**: Access sequence IDs, descriptions, lengths, annotations, and features like CDS or gene locations.
- **🎨 Modern Web Interface**: A responsive, DNA-themed UI with collapsible sections for easy data exploration.
- **⚡ Biopython Power**: Uses Entrez and SeqIO for robust, reliable sequence fetching.
- **🔬 Detailed Feature Analysis**: Extracts start positions for coding sequences and other genomic features.
- **💻 Lightweight & Fast**: Built with Flask and minimal dependencies for quick deployment.

## 🚀 Getting Started

### Prerequisites
- Python 3.6+
- A valid email for NCBI Entrez API (required for compliance).
- A curiosity for molecular biology! 🧬

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/husnain002/enzyme-sequence-finder.git
   cd enzyme-sequence-finder
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask biopython
   ```

4. Configure your NCBI Entrez email:
   - Open `app.py` and update the email:
     ```python
     Entrez.email = "your.email@example.com"
     ```

5. Ensure templates are in place:
   - The `templates` folder must contain `index.html` and `results.html` (already provided in your project).
   - Place them in the `templates` directory if not already present.

6. Run the application:
   ```bash
   python app.py
   ```

7. Open your browser and visit `http://127.0.0.1:5000` to start exploring enzyme sequences.

### Usage
- **Search for Sequences**:
  1. Enter an organism (e.g., "Bacillus siamensis") and enzyme (e.g., "cellulase").
  2. Select sequence type(s): Nucleotide, Protein, or both.
  3. Click "Search" to retrieve sequence data.
- **Explore Results**: View sequence details, annotations, features, and raw GenBank records in collapsible sections.
- **Navigate**: Use the "Back to Search" link to try new queries.
- **Stop the Server**: Press `Ctrl+C` in the terminal to shut down.

## 🎨 Screenshots

![image](https://github.com/user-attachments/assets/d64422b0-91e6-4d15-8040-71526347210a)

![image](https://github.com/user-attachments/assets/ad29556d-83a9-40d8-99e8-e70fb48ec3de)

![image](https://github.com/user-attachments/assets/ad6bbced-8ab9-4b7d-887c-7e09e42ca830)

![image](https://github.com/user-attachments/assets/3aa9aef4-177e-470e-82cd-86ab59149416)

*Explore enzyme sequences with a sleek, DNA-inspired interface!*

## 🛠️ How It Works
Enzyme Sequence Finder leverages Flask for its web framework and Biopython for NCBI database access:
- **Search Logic**: Queries NCBI’s nucleotide and protein databases using organism and enzyme terms.
- **Data Retrieval**: Fetches GenBank records via `Entrez.efetch` and parses them with `SeqIO`.
- **Feature Extraction**: Identifies key features like CDS start positions and annotations.
- **Interface**: Renders a modern UI with `index.html` for input and `results.html` for detailed, collapsible output.

The application respects NCBI’s API guidelines with a 1-second delay between requests and requires a valid email for Entrez access.

## 🔬 Contributing
Want to amplify the molecular insights? Contributions are welcome!
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/enzyme-analyzer`).
3. Make changes and commit (`git commit -m "Added enzyme comparison feature"`).
4. Push to the branch (`git push origin feature/enzyme-analyzer`).
5. Open a Pull Request.

See [CONTRIBUTING.md](CONTRIBUTING.md) and check [Issues](https://github.com/husnain002/enzyme-sequence-finder/issues) for ideas.

## ⚠️ Notes
- **NCBI Compliance**: Always use a valid email for Entrez API to avoid access restrictions.
- **Rate Limiting**: A 1-second delay is included to comply with NCBI’s API rules.
- **Local Deployment**: Runs in debug mode on `http://127.0.0.1:5000`. For production, use a WSGI server like Gunicorn.
- **Templates**: Ensure `index.html` and `results.html` are in the `templates` folder.
- **Dependencies**: Requires Flask and Biopython. Install via `pip`.

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments
- Powered by [Biopython](https://biopython.org/) and [Flask](https://flask.palletsprojects.com/).
- Inspired by the beauty of enzymes and the precision of DNA replication.
- Thanks to NCBI for providing open-access genomic data.

---

**Decode the enzymes of life!** 🧬 Star this repo if you’re passionate about bioinformatics and sequence discovery! ⭐﻿# enzyme-search
