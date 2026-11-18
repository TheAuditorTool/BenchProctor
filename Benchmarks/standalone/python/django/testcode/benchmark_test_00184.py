# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


def BenchmarkTest00184(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
