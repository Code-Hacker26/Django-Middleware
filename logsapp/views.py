import matplotlib.pyplot as plt
from django.http import HttpResponse
from django.shortcuts import render
from io import BytesIO
from .models import RequestLog,LogEntry

def logs_graph(request):
    success_count = RequestLog.objects.filter(status_code__lt=400).count()  
    error_count = RequestLog.objects.filter(status_code__gte=400).count()

    labels = ['Success', 'Error']
    values = [success_count, error_count]
    colors = ['green', 'red']

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=colors)
    plt.title('Request Status Breakdown')
    plt.ylabel('Count')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    return HttpResponse(buffer, content_type='image/png')


def logs_list_view(request):
    
    logs = LogEntry.objects.all().order_by('-timestamp')  # Most recent logs first
    return render(request, 'logs_list.html', {'logs': logs})