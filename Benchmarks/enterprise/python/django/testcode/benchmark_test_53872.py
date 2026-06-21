# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest53872(request):
    upload_name = request.FILES['upload'].name
    return HttpResponse('<!-- diagnostic build token: ' + str(upload_name) + ' -->', content_type='text/html')
