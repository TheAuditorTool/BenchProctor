# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest11757(request):
    multipart_value = request.POST.get('multipart_field', '')
    parts = []
    for token in str(multipart_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
