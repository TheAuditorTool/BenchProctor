# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest60421(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % str(auth_header)
    return HttpResponse('<html><body><h1>' + str(data) + '</h1></body></html>', content_type='text/html')
