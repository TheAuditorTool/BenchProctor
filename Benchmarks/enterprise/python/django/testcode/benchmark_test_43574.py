# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest43574(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    with open('/var/app/data/' + str(auth_header), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
