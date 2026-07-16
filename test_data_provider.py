from data_provider import get_drug_data, get_research_papers, get_electrochemical_data
import json

def test():
    drug = "Metoclopramide"
    print(f"--- Testing Drug Data for {drug} ---")
    data = get_drug_data(drug)
    print(json.dumps(data, indent=2))
    
    print(f"\n--- Testing Research Papers for {drug} ---")
    papers = get_research_papers(drug)
    print(f"Found {len(papers)} papers.")
    if papers:
        print(f"First paper title: {papers[0]['title']}")
    
    print(f"\n--- Testing Electrochemical Data for {drug} ---")
    ec_data = get_electrochemical_data(drug)
    print(json.dumps(ec_data, indent=2))

if __name__ == "__main__":
    test()
