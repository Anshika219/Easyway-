# Code_Fusion
AI based expenses tracker
```mermaid
Graph TD
    A[User] --> B[Frontend UI<br/>(React / Streamlit)];
    B --> C[FastAPI Backend];
    C --> D[AI Processing Layer];
    D --> D1[OCR];
    D --> D2[Speech-to-Text];
    D --> D3[LLM];
    D --> E[Expense Data Structuring];
    E --> F[Budget Details Generation];
    F --> G[Frontend Display];
```
