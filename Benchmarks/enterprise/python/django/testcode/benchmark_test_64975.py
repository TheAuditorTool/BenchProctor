# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest64975(request):
    upload_name = request.FILES['upload'].name
    data = coalesce_blank(upload_name)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
