# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest26690(request):
    upload_name = request.FILES['upload'].name
    return JsonResponse({'error': str(upload_name), 'stack': repr(locals())}, status=500)
