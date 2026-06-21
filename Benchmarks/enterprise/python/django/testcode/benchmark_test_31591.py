# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest31591(request):
    upload_name = request.FILES['upload'].name
    with open('/var/app/data/' + str(upload_name), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
