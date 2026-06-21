# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest60038(request):
    upload_name = request.FILES['upload'].name
    return HttpResponse(mark_safe('<div>' + str(upload_name) + '</div>'))
