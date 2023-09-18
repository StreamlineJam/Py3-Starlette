from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

import uvicorn

async def homepage(request):
    return JSONResponse({"Hello": "world"})

async def about(request):
    return JSONResponse({"message": "shit balls its the python monster!!!!"})

async def contact(request):
    return JSONResponse({"my social security number": "1234567890"})

app = Starlette(
    debug=True,
    routes=[
        Route('/', homepage),
        Route('/about', about),
        Route("/contact",  contact)
    ]
)

uvicorn.run(app, port=8080)