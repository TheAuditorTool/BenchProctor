# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponseRedirect


def BenchmarkTest00095(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    return HttpResponseRedirect(str(data))
