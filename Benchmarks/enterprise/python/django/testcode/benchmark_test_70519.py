# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest70519(request):
    multipart_value = request.POST.get('multipart_field', '')
    with open('/var/app/data/' + str(multipart_value), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
