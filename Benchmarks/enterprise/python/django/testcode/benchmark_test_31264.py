# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31264(request, path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
