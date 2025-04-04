# Passage Difficulty Analyzer

A sophisticated tool for analyzing the difficulty and complexity of reading passages for the SAT and other standardized tests. This tool uses quantitative metrics and AI-powered analysis to provide comprehensive insights into passage complexity across multiple dimensions.

## 🚀 Features

- **Multi-dimensional Analysis**: Evaluates passages across 7 key categories:
  - Readability (Lexile, Flesch-Kincaid, etc.)
  - Vocabulary Complexity
  - Syntactic Complexity
  - Conceptual Density
  - Rhetorical Structure
  - Content Accessibility
  - Cognitive Demands

- **AI-Powered Insights**: Uses Anthropic's Claude API to perform qualitative analyses that go beyond traditional readability formulas

- **Parallel Processing**: Optimized with concurrent API calls for faster analysis of multiple passages

- **Resilient Architecture**: Includes retry mechanisms and progress tracking to handle API rate limits

## 📊 Analysis Metrics

The analyzer evaluates passages on these specific metrics:

### Readability
- Lexile Measure
- Flesch-Kincaid Grade Level
- Average Sentence Length

### Vocabulary
- Vocabulary Difficulty Ratio
- Academic Word Usage
- Domain-Specific Terminology

### Syntactic Complexity
- Subordinate Clauses
- Syntactic Variety
- Structural Inversions
- Embedded Clauses

### Conceptual Density
- Abstraction Level
- Concept Familiarity
- Implied Information

### Rhetorical Structure
- Argumentative Complexity
- Organizational Clarity
- Transitional Elements

### Content Accessibility
- Prior Knowledge Requirements
- Disciplinary Perspective
- Language Modernity

### Cognitive Demands
- Inference Requirement
- Figurative Language
- Author's Purpose

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/sat-passage-analyzer.git
cd sat-passage-analyzer

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 📝 Usage

### Basic Usage

```python
from sat_passage_analyzer import SATPassageAnalyzer

# Initialize the analyzer
analyzer = SATPassageAnalyzer()

# Load passages
passages = analyzer.load_data("your_passages.json", file_type="json")
# Or for CSV: passages = analyzer.load_data("your_passages.csv", file_type="csv")

# Set up API key
analyzer.init_anthropic_client(api_key="your-anthropic-api-key")

# Run analysis
results = analyzer.evaluate_passages()

# Generate reports
reports = analyzer.generate_report(output_dir="results")
```

### Parallel Processing

```python
from parallelized_analyzer import *

# Set number of parallel workers
max_workers = 3

# Run analysis with parallelization and retries
results = analyzer.evaluate_passages_parallel(max_workers=max_workers)
```

### Input Format

JSON input should follow this structure:
```json
[
  {
    "id": "passage1",
    "title": "Sample Passage 1",
    "text": "Full text of the passage..."
  },
  {
    "id": "passage2",
    "title": "Sample Passage 2",
    "text": "Full text of the passage..."
  }
]
```

CSV input should have columns for `id`, `title`, and `text`.

## 📈 Example Results

The analyzer provides a comprehensive difficulty score on a scale of 1-10, along with detailed metrics across all categories:

```json
{
  "passage_id": "passage1",
  "title": "Sample Passage 1",
  "overall_score": 7.8,
  "category_scores": {
    "readability": 8.2,
    "vocabulary": 7.5,
    "syntactic_complexity": 8.0,
    "conceptual_density": 7.9,
    "rhetorical_structure": 6.8,
    "content_accessibility": 7.5,
    "cognitive_demands": 8.4
  }
}
```
