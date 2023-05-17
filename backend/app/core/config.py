class Settings:
    API_PREFIX: str = ""

    # DB_DIALECT: str = ""
    # DB_USERNAME: str = ""
    # DB_PASSWORD: str = ""
    # DB_HOST: str = ""
    # DB_PORT: int = 0
    # DATABASE: str = ""
    # DB_URL: str = f"{DB_DIALECT}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}"
    DB_URL = "sqlite:///app.db"

    INIT_USERNAME: str = ""
    INIT_PASSWORD: str = ""
    INIT_EMAIL: str = ""


settings = Settings()
