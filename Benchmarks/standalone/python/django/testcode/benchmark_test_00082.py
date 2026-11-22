# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00082(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    reader = make_reader(forwarded_ip)
    data = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    resp = HttpResponse(content_type='text/html')
    resp.write('<div>' + str(processed) + '</div>')
    return resp
