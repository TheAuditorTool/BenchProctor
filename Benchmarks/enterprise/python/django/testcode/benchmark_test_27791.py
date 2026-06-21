# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27791(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
