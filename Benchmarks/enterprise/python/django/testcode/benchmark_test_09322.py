# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09322(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
