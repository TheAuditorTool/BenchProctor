# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31711(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
