# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
from django.http import HttpResponse


request_state: dict[str, str] = {}

def BenchmarkTest25951(request):
    upload_name = request.FILES['upload'].name
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse('<script src="' + str(processed) + '"></script>', content_type='text/html')
