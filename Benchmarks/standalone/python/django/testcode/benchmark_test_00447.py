# SPDX-License-Identifier: Apache-2.0
from django.utils.safestring import mark_safe
from django.http import HttpResponse


def BenchmarkTest00447(request):
    field_value = request.POST.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    return HttpResponse(mark_safe('<div>' + str(data) + '</div>'))
