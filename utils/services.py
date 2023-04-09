from settings import settings

def get_service_details():
    return {
        "title": settings.SERVICE_NAME,
        "description": f"""Mime Test 🛠️ API's<br><strong>Debug Info</strong>\
        <br>Instance: {settings.API_INSTANCE} \
        <br>Version: {settings.VERSION}""",
        "version": settings.VERSION,
    }