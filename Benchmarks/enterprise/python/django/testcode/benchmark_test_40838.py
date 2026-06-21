# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40838(request):
    multipart_value = request.POST.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
