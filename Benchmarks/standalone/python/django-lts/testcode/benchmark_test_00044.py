# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse


def BenchmarkTest00044(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
