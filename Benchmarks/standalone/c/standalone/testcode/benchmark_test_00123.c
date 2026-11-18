// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

struct c_payload { const char *value; };

void benchmark_test_00123(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    FILE *_src_fp = fopen("/etc/app/config", "r");
    if (_src_fp != NULL) {
        if (fgets(user_input_buf, sizeof(user_input_buf), _src_fp) == NULL) user_input_buf[0] = '\0';
        fclose(_src_fp);
    }
    const char *user_input = user_input_buf;
    struct c_payload _pd;
    _pd.value = user_input;
    const char *data = _pd.value;
    char _buf[16] = "fixedcontent12";
    size_t _span = (size_t)strtoul(data, NULL, 10);
    unsigned int _sum = 0;
    for (size_t _k = 0; _k < _span; _k++) _sum += (unsigned char)_buf[_k];
    printf("%u\n", _sum);
}
