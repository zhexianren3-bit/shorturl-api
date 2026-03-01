from fastapi import FastAPI
app = FastAPI()
urls = {}
@app.get("/")
def root(): return {"msg": "短链接API"}
@app.post("/shorten")
def shorten(url: str):
    import random, string
    code = ''.join(random.choices(string.ascii_letters, k=6))
    urls[code] = url
    return {"success": True, "short_url": f"https://short.io/{code}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
