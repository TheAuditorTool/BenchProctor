# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61579(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    trusted_claim = str(processed)
    return JsonResponse({'trusted': trusted_claim}, status=200)
