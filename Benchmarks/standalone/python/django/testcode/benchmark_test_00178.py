# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import re


def BenchmarkTest00178(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % (ua_value,)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
