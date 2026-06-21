# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest73817(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
