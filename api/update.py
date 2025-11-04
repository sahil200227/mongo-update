def handler(request, response):
    response.status_code = 200
    response.send("✅ update.py was found and is running on Vercel")
