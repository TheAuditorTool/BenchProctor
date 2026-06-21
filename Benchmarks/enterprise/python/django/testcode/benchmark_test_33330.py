# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


request_state: dict[str, str] = {}

def BenchmarkTest33330(request):
    upload_name = request.FILES['upload'].name
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
