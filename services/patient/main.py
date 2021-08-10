import os
import uvicorn
from api import app

MODE = os.getenv("MODE", "dev").lower()
PORT = os.getenv("PORT", 8000)


if __name__ == "__main__":
    if MODE == "dev":
        uvicorn.run(app, host="0.0.0.0", port=PORT, log_level="debug")
    elif MODE == "prod":
        uvicorn.run(app, host="0.0.0.0", port=PORT, log_level="error")
    else:
        print(f"Invalid MODE type! {MODE=}")
