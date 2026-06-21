# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re
from django.http import HttpResponse
import ast


def BenchmarkTest30900(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse('<script src="' + str(processed) + '"></script>', content_type='text/html')
