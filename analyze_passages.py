# analyze_passages.py
from sat_passage_analyzer import SATPassageAnalyzer
# Import our parallelized functions
from parallelized_analyzer import *
import time
import os

def main():
    start_time = time.time()
    
    # Initialize the analyzer
    analyzer = SATPassageAnalyzer()
    
    # Load data
    passages = analyzer.load_data("fixed-passages-analyze.json", file_type="json")
    print(f"Loaded {len(analyzer.passages)} passages")
    
    # Set your Anthropic API key
    analyzer.init_anthropic_client(api_key="")
    
    # Set the number of parallel workers (adjust based on API rate limits)
    max_workers = 5  # Start with a conservative number to avoid hitting rate limits
    
    # Calculate readability metrics (non-API dependent)
    print("\n=== Calculating Readability Metrics ===")
    try:
        lexile = analyzer.calculate_lexile_scores_parallel(max_workers=max_workers)
    except Exception as e:
        print(f"Error calculating Lexile scores: {e}")
    
    fk = analyzer.calculate_flesch_kincaid()
    asl = analyzer.calculate_avg_sentence_length()
    
    # Calculate vocabulary metrics (non-API dependent)
    print("\n=== Calculating Vocabulary Metrics ===")
    try:
        vocab_difficulty = analyzer.calculate_vocabulary_difficulty_ratio()
        academic_usage = analyzer.calculate_academic_word_usage()
    except Exception as e:
        print(f"Error calculating vocabulary metrics: {e}")
    
    # Now use the parallel functions for the API-dependent metrics
    
    # Domain-specific terminology
    domain_specific = analyzer.calculate_domain_specific_terminology_parallel(max_workers=max_workers)
    
    # Syntactic complexity
    subordinate = analyzer.calculate_subordinate_clauses_parallel(max_workers=max_workers)
    syntax_variety = analyzer.calculate_syntactic_variety_parallel(max_workers=max_workers)
    inversions = analyzer.calculate_structural_inversions_parallel(max_workers=max_workers)
    embedded = analyzer.calculate_embedded_clauses_parallel(max_workers=max_workers)
    
    # Conceptual density
    abstraction = analyzer.calculate_abstraction_level_parallel(max_workers=max_workers)
    familiarity = analyzer.calculate_concept_familiarity_parallel(max_workers=max_workers)
    implied = analyzer.calculate_implied_information_parallel(max_workers=max_workers)
    
    # Rhetorical structure
    argumentative = analyzer.calculate_argumentative_complexity_parallel(max_workers=max_workers)
    organizational = analyzer.calculate_organizational_clarity_parallel(max_workers=max_workers)
    transitional = analyzer.calculate_transitional_elements_parallel(max_workers=max_workers)
    
    # Content accessibility
    prior_knowledge = analyzer.calculate_prior_knowledge_requirements_parallel(max_workers=max_workers)
    disciplinary = analyzer.calculate_disciplinary_perspective_parallel(max_workers=max_workers)
    language_modernity = analyzer.calculate_language_modernity_parallel(max_workers=max_workers)
    
    # Cognitive demands
    inference = analyzer.calculate_inference_requirement_parallel(max_workers=max_workers)
    figurative = analyzer.calculate_figurative_language_parallel(max_workers=max_workers)
    authors = analyzer.calculate_authors_purpose_parallel(max_workers=max_workers)
    
    # Calculate overall difficulty
    print("\n=== Calculating Overall Difficulty Scores ===")
    overall_scores = analyzer.calculate_overall_difficulty()
    
    # Generate reports
    report_paths = analyzer.generate_report(output_dir="results")
    
    end_time = time.time()
    print(f"Analysis complete! Reports saved to: {report_paths}")
    print(f"Total execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
