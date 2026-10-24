from fastapi import FastAPI, UploadFile, File
import time, os, zlib
from v8 import NexusV8_GodSqueezer

app = FastAPI(title="☠️ NEXUS V8 - 22GB->2GB GOD SQUEEZER")

v8_engine = NexusV8_GodSqueezer()

@app.get("/")
def home():
    return {
        "engine": "NEXUS V8 ONLY",
        "power": "22GB -> 2GB",
        "file": "v8.py",
        "status": "GOD MODE LIVE 🔥",
        "docs": "/docs"
    }

@app.get("/v8/info")
def v8_info():
    return {
        "file": "v8.py",
        "class": "NexusV8_RealSqueezer",
        "power": "22GB -> 2GB in ~180s",
        "speed": "80 MB/s | 11x Ratio",
        "chunk": "4MB | Level 1",
        "status": "ONLY V8 - NO V7"
    }

@app.post("/v8/squeeze")
async def v8_squeeze(file: UploadFile = File(...)):
    temp_in = f"/tmp/{file.filename}"
    temp_out = f"/tmp/{file.filename}.nexus"
    
    with open(temp_in, "wb") as f:
        f.write(await file.read())
    
    start = time.time()
    v8_engine.squeeze_file(temp_in, temp_out)
    elapsed = time.time() - start
    
    size_in = os.path.getsize(temp_in)
    size_out = os.path.getsize(temp_out)
    
    return {
        "input": f"{size_in/1024**2:.2f} MB",
        "output": f"{size_out/1024**2:.2f} MB",
        "ratio": f"{size_in/size_out:.1f}x KILLED!",
        "time": f"{elapsed:.2f}s",
        "engine": "V8 ONLY"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
