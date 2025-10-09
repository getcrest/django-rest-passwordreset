import os

def get_referer_meta(request):
    # HTTP_REFERER
    referer = str(request.META.get("HTTP_REFERER"))

    meta = {}

    if (os.environ.get("QUANTUM_PORTAL_NAME", "portal") in referer):
        return "portal"
    
    return "app"