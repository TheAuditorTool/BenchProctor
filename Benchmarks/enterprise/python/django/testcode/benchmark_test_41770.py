# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41770(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
