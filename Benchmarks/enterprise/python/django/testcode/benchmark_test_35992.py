# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest35992(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % (upload_name,)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
