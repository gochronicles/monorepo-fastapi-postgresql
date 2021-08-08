import os
import uvicorn
from api import app

MODE = os.getenv("MODE", "dev").lower()

if __name__ == "__main__":
    if MODE == "dev":
        uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
    elif MODE == "prod":
        uvicorn.run(app, host="0.0.0.0", port=8000, log_level="error")
    else:
        print(f"Invalid MODE type! {MODE=}")
