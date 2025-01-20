# Personalised Product Recommendation System

This repository contains a personalised product recommendation system that leverages **FAISS** for similarity-based recommendations and **FastAPI** for deployment. The application provides recommendations for users based on content-based and collaborative filtering approaches and ensures diversity and relevance in suggestions.

## Features

- **Content-Based Filtering**: Uses product features like ratings and discounts to recommend similar items.
- **Collaborative Filtering**: Recommends products by analysing user-product interactions.
- **Hybrid Recommendation System**: Combines content-based and collaborative filtering for better accuracy and diversity.
- **FAISS Integration**: Utilises FAISS for efficient similarity search.
- **REST API**: Built with FastAPI to provide endpoints for querying recommendations.
- **Dockerised Deployment**: Includes Docker support for easy deployment.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Aubur9y/Personalised-Product-Recommendation-System.git

   cd Personalised-Product-Recommendation-System

2. Build and run the Docker container:

    ```bash
    docker build -t personalised-recommendation-app .

    docker run -d -p 8000:8000 personalised-recommendation-app

3. Alternatively, set up the environment locally:
    
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    uvicorn app:app --reload

## API Endpoints
### Get Recommendations:
- URL: /recommend/
- Method: GET
- Parameters:
    - user_index (int): The index of the user to get recommendations for.
    - top_n (int): Number of recommendations to return.
- Example:
    ```bash
    curl "http://localhost:8000/recommend/?user_index=0&top_n=5"
- Response
    ```bash
    {
        "user_index": 0,
        "recommendations": [
            {"product_id": 132, "score": 1.0},
            {"product_id": 113, "score": 0.9}
        ]
    }

## Future Enhancements
- Integrate Apache Spark for scalable collaborative filtering.
- Support for dynamic user interaction and feedback integration.
- Improved diversity logic for better recommendations across different product categories.
