from fastapi import Request

def get_tenant_id(request: Request):

    return request.headers.get("X-Tenant-ID")
