import logging
from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from logsapp.models import RequestLog, LogEntry

logger = logging.getLogger(__name__)

class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Store start time of the request
        request.start_time = datetime.now()

    def process_response(self, request, response):
        # Calculate the duration of the request
        duration = None
        if hasattr(request, 'start_time'):
            duration = (datetime.now() - request.start_time).total_seconds()

        # Save log to RequestLog model
        RequestLog.objects.create(
            path=request.path,
            method=request.method,
            status_code=response.status_code,
            duration=duration,
            timestamp=datetime.now()
        )

        # Save log to LogEntry model
        LogEntry.objects.create(
            path=request.path,
            method=request.method,
            status_code=response.status_code,
            timestamp=datetime.now()
        )

        return response

    def process_exception(self, request, exception):
        logger.error(f"Exception occurred: {exception}", exc_info=True)
        
        # Log the exception to the RequestLog model
        RequestLog.objects.create(
            path=request.path,
            method=request.method,
            status_code=500,
            error_message=str(exception),
            timestamp=datetime.now()
        )

        # Log the exception to the LogEntry model
        LogEntry.objects.create(
            path=request.path,
            method=request.method,
            status_code=500,
            timestamp=datetime.now()
        )

        return None
