# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest78586(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    return HttpResponse(mark_safe('<div>' + str(referer_value) + '</div>'))
