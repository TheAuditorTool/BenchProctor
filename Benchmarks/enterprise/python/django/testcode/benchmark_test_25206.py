# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest25206(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    return HttpResponse(mark_safe('<div>' + str(origin_value) + '</div>'))
