# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
import ast


def BenchmarkTest26531(request):
    upload_name = request.FILES['upload'].name
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')
