# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30612(request):
    multipart_value = request.POST.get('multipart_field', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(multipart_value)})
