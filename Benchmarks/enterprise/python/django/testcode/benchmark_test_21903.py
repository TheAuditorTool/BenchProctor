# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21903(request):
    multipart_value = request.POST.get('multipart_field', '')
    if multipart_value not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = multipart_value
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(processed)})
