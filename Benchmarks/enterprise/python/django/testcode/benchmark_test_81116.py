# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def to_text(value):
    return str(value).strip()

def BenchmarkTest81116(request):
    upload_name = request.FILES['upload'].name
    data = to_text(upload_name)
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
