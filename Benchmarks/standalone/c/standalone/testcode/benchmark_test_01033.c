// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>
#include <regex.h>

typedef struct ldap LDAP;
typedef struct ldapmsg LDAPMessage;
#define LDAP_SCOPE_SUBTREE 2
#define LDAP_OPT_PROTOCOL_VERSION 0x0011
#define LDAP_VERSION3 3
extern int ldap_initialize(LDAP **_ldp, const char *_uri);
extern int ldap_set_option(LDAP *_ld, int _option, const void *_invalue);
extern int ldap_simple_bind_s(LDAP *_ld, const char *_who, const char *_passwd);
extern int ldap_search_ext_s(LDAP *_ld, const char *_base, int _scope, const char *_filter, char **_attrs, int _attrsonly, void *_sc, void *_cc, void *_tmo, int _slim, LDAPMessage **_res);

void benchmark_test_01033(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *data = "";
    if (strlen(user_input) > 0) data = user_input;
    regex_t _re;
    const char *safe = data;
    if (regcomp(&_re, "^(asc|desc|name|created)$", REG_EXTENDED) == 0) {
        if (regexec(&_re, data, 0, NULL, 0) != 0) safe = "asc";
        regfree(&_re);
    }
    LDAP *_ld = NULL;
    const char *_ldap_url = getenv("LDAP_URL");
    ldap_initialize(&_ld, _ldap_url != NULL ? _ldap_url : "ldap://directory:1389");
    int _ldap_version = LDAP_VERSION3;
    ldap_set_option(_ld, LDAP_OPT_PROTOCOL_VERSION, &_ldap_version);
    ldap_simple_bind_s(_ld, NULL, NULL);
    char _filter[512];
    snprintf(_filter, sizeof(_filter), "(uid=%s)", safe);
    LDAPMessage *_res = NULL;
    ldap_search_ext_s(_ld, "ou=people,dc=example,dc=com", LDAP_SCOPE_SUBTREE, _filter, NULL, 0, NULL, NULL, NULL, 0, &_res);
}
