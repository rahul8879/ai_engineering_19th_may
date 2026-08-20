from pydantic_settings import BaseSettings, SettingsConfigDict

from paths import ENV_FILES

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILES,
        case_sensitive=False,
        extra="ignore"
    )

    openai_api_key: str
    openai_embedding_model: str = "text-embedding-3-small"
    openai_llm_model: str = "gpt-4o-mini"
    openai_embedding_dimensions: int = 1536

    pinecone_api_key: str
    pinecone_index_name: str = "hireflow-resumes"
    pinecone_jd_index_name: str = "hireflow-jd"
    # Serverless indexes need a cloud + region; aws/us-east-1 is the free tier.
    pinecone_cloud: str = "aws"
    pinecone_region: str = "us-east-1"


    # ── Redis ───────────────────────────────────────────────────────
    redis_url: str = "redis://localhost:6379/0"

    # ── MLflow ──────────────────────────────────────────────────────
    mlflow_tracking_uri: str = "http://localhost:5000"
    mlflow_experiment_name: str = "hireflow-evaluations"

    # ── App ─────────────────────────────────────────────────────────
    app_env: str = "development"
    top_k: int = 5
    min_confidence: float = 0.3


settings = Settings()




