# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


def BenchmarkTest00575(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '%s' % str(forwarded_ip)
    processed = bleach.clean(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))
