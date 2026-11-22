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
struct berval { unsigned long bv_len; char *bv_val; };
#define LDAP_COMPARE_TRUE 6
extern int ldap_compare_ext_s(LDAP *_ld, const char *_dn, const char *_attr, struct berval *_value, void *_sc, void *_cc);
extern int ldap_unbind_ext_s(LDAP *_ld, void *_sc, void *_cc);
static const char *c_passthrough(const char *s) { while (*s == ' ') s++; return s; }

void benchmark_test_00222(int argc, char **argv)
{
    const char *user_input = (argc > 2) ? argv[2] : "";
    const char *(*_fn)(const char *) = c_passthrough;
    const char *data = _fn(user_input);
    regex_t _re;
    const char *arg = data;
    if (regcomp(&_re, "^[a-zA-Z0-9 #%._-]+$", REG_EXTENDED) == 0) {
        if (regexec(&_re, data, 0, NULL, 0) != 0) arg = "config";
        regfree(&_re);
    }
    LDAP *_ld = NULL;
    const char *_ldap_url = getenv("LDAP_URL");
    ldap_initialize(&_ld, _ldap_url != NULL ? _ldap_url : "ldap://directory:1389");
    int _ldap_version = LDAP_VERSION3;
    ldap_set_option(_ld, LDAP_OPT_PROTOCOL_VERSION, &_ldap_version);
    ldap_simple_bind_s(_ld, NULL, NULL);
    char _dn[512];
    snprintf(_dn, sizeof(_dn), "uid=%s,ou=people,dc=example,dc=com", arg);
    struct berval _role = { 5, (char *)"admin" };
    int _rc = ldap_compare_ext_s(_ld, _dn, "employeeType", &_role, NULL, NULL);
    printf("%s\n", _rc == LDAP_COMPARE_TRUE ? "admin" : "user");
    ldap_unbind_ext_s(_ld, NULL, NULL);
}
