import pandas as pd
import numpy as np
from typing import List, Dict

class RecommendationEngine:
    def __init__(self):
        self.packages_df = None
        self.tfidf_matrix = None
        
    def tfidf_vectorize(self, text: str, text_features: List[str]) -> np.ndarray:
        """Custom implementation of TF-IDF vectorization"""
        term_freq = {}
        for term in text.split():
            term_freq[term] = term_freq.get(term, 0) + 1
        
        # Compute TF-IDF scores
        tfidf_vector = np.zeros(len(text_features))
        for idx, term in enumerate(text_features):
            if term in term_freq:
                tfidf_vector[idx] = term_freq[term] * np.log(len(text_features) / sum([term in doc.split() for doc in text_features]))
        return tfidf_vector

    def train(self, packages: List[Dict]):
        """Train the recommendation engine with travel packages"""
        self.packages_df = pd.DataFrame(packages)
        
        # Create text features from package descriptions
        text_features = self.packages_df['description'] + ' ' + self.packages_df['destination']
        all_terms = list(set(' '.join(text_features).split()))  # Get unique terms
        
        # Create TF-IDF matrix
        self.tfidf_matrix = np.array([self.tfidf_vectorize(text, all_terms) for text in text_features])
        
    def get_recommendations(self, package_id: int, num_recommendations: int = 5) -> List[Dict]:
        """Get similar package recommendations"""
        if self.tfidf_matrix is None:
            raise ValueError("Model not trained yet")
            
        package_idx = self.packages_df[self.packages_df['id'] == package_id].index[0]
        
        # Compute cosine similarity
        similarities = np.dot(self.tfidf_matrix, self.tfidf_matrix[package_idx])
        similar_packages = similarities.argsort()[-num_recommendations-1:-1][::-1]
        
        recommendations = self.packages_df.iloc[similar_packages].to_dict('records')
        return recommendations

# Example usage
packages = [
    {"id": 1, "description": "Beach holiday in Bali", "destination": "Bali"},
    {"id": 2, "description": "Adventure in the Himalayas", "destination": "Himalayas"},
    {"id": 3, "description": "Romantic getaway in Paris", "destination": "Paris"},
    {"id": 4, "description": "Safari in Africa", "destination": "Africa"},
    {"id": 5, "description": "Ski trip to the Swiss Alps", "destination": "Switzerland"}
]

engine = RecommendationEngine()
engine.train(packages)
print(engine.get_recommendations(1, 3))  # Get recommendations for the package with id 1
