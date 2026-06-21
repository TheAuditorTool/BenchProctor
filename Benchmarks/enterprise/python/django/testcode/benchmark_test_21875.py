# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


def BenchmarkTest21875(request):
    host_value = request.META.get('HTTP_HOST', '')
    processed = bleach.clean(host_value)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
