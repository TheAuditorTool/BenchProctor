# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


def BenchmarkTest61902(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    processed = bleach.clean(forwarded_ip)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
