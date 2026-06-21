# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81124(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
