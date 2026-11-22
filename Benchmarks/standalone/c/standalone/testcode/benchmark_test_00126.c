// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

struct c_plan { const char *name; int limit; };
static int c_plan_cmp(const void *_key, const void *_entry) { return strcmp((const char *)_key, ((const struct c_plan *)_entry)->name); }

void benchmark_test_00126(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    if (fgets(user_input_buf, sizeof(user_input_buf), stdin) == NULL) user_input_buf[0] = '\0';
    user_input_buf[strcspn(user_input_buf, "\n")] = '\0';
    const char *user_input = user_input_buf;
    char data[512];
    size_t _li = 0;
    for (; user_input[_li] != '\0' && _li < sizeof(data) - 1; ++_li) data[_li] = user_input[_li];
    data[_li] = '\0';
    static const struct c_plan _plans[] = { { "basic", 10 }, { "enterprise", 1000 }, { "pro", 100 } };
    const struct c_plan *_plan = bsearch(data, _plans, sizeof(_plans) / sizeof(_plans[0]), sizeof(_plans[0]), c_plan_cmp);
    int _limit = _plan != NULL ? _plan->limit : 0;
    printf("limit %d\n", _limit);
}
