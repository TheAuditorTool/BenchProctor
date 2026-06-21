# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest10904(request):
    host_value = request.META.get('HTTP_HOST', '')
    return HttpResponse(mark_safe('<div>' + str(host_value) + '</div>'))
