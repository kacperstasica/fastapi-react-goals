import logging
import time
from pathlib import Path

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


def setup_logger() -> logging.Logger:
    """Configure and return the access logger"""
    Path("logs").mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logs/access.log", mode='a'),
            logging.StreamHandler()
        ]
    )
    
    return logging.getLogger("access")


logger = setup_logger()


class LoggingMiddleware(BaseHTTPMiddleware):
    """Custom middleware to log HTTP requests"""
    
    def __init__(self, app, logger: logging.Logger):
        super().__init__(app)
        self.logger = logger
    
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        self.logger.info(
            f'{request.client.host} - "{request.method} {request.url.path}" - START'
        )
        
        response = await call_next(request)
        
        duration = time.time() - start_time
        self.logger.info(
            f'{request.client.host} - "{request.method} {request.url.path}" '
            f'{response.status_code} - {duration:.3f}s'
        )
        
        return response

