# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse


def BenchmarkTest19516(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(str(processed), content_type='text/html')
