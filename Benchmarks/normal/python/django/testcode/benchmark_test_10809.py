# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10809(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
