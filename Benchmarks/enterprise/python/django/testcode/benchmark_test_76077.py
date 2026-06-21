# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest76077(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
