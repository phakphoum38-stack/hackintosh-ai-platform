from fastapi import Request

async def get_tenant(request: Request):

    return request.headers.get("X-Tenant-ID")
