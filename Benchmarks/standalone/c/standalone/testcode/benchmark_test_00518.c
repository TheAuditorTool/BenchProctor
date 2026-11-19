// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

void benchmark_test_00518(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    if (fgets(user_input_buf, sizeof(user_input_buf), stdin) == NULL) user_input_buf[0] = '\0';
    user_input_buf[strcspn(user_input_buf, "\n")] = '\0';
    const char *user_input = user_input_buf;
    const char *safe = user_input;
    if (strcmp(user_input, "/bin/echo") != 0 && strcmp(user_input, "/bin/cat") != 0) safe = "/bin/echo";
    char _cmd[512];
    snprintf(_cmd, sizeof(_cmd), "grep %s /var/log/app.log", safe);
    FILE *_p = popen(_cmd, "r");
    if (_p) pclose(_p);
}
