# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest32305(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    return HttpResponse(mark_safe('<div>' + str(auth_header) + '</div>'))
