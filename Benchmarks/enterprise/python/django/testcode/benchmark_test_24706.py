# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest24706(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    return HttpResponse(mark_safe('<div>' + str(header_value) + '</div>'))
