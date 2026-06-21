# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50954(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = '%s' % (multipart_value,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
