# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest55534(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '%s' % (forwarded_ip,)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
