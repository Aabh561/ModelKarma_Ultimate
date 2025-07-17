from fastapi import FastAPI
from api.routes import karma

app = FastAPI(title="ModelKarma API")
app.include_router(karma.router)
