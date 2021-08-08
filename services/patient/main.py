import os
import uvicorn
from api import app

workers = os.cpu_count()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="error", workers=workers)
