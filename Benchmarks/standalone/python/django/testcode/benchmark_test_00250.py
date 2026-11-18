# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse


def BenchmarkTest00250(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value!s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
