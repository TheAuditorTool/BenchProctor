# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest52205(request):
    upload_name = request.FILES['upload'].name
    data = default_blank(upload_name)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
