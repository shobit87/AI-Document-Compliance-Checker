import tempfile
import asyncio
from fastapi import UploadFile

async def write_temp_file(file: UploadFile) -> str:
    """Save uploaded file to a temp path and return its location."""
    suffix = "." + file.filename.split(".")[-1] if "." in file.filename else ""
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        return tmp.name

async def run_blocking(func, *args, **kwargs):
    """Run a blocking (non-async) function in a thread pool."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, func, *args, **kwargs)
