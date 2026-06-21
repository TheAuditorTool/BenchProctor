# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46599(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})
