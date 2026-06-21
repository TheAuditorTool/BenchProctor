# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09420(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % (header_value,)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return JsonResponse({"saved": True})
