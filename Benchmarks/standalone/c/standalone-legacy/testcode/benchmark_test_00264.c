// SPDX-License-Identifier: Apache-2.0
#define _XOPEN_SOURCE 700
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <stdint.h>
#include <time.h>

typedef struct ldap LDAP;
typedef struct ldapmsg LDAPMessage;
#define LDAP_SCOPE_SUBTREE 2
#define LDAP_OPT_PROTOCOL_VERSION 0x0011
#define LDAP_VERSION3 3
extern int ldap_initialize(LDAP **_ldp, const char *_uri);
extern int ldap_set_option(LDAP *_ld, int _option, const void *_invalue);
extern int ldap_simple_bind_s(LDAP *_ld, const char *_who, const char *_passwd);
extern int ldap_search_ext_s(LDAP *_ld, const char *_base, int _scope, const char *_filter, char **_attrs, int _attrsonly, void *_sc, void *_cc, void *_tmo, int _slim, LDAPMessage **_res);
#define LDAP_MSG_ALL 1
extern int ldap_search_ext(LDAP *_ld, const char *_base, int _scope, const char *_filter, char **_attrs, int _attrsonly, void *_sc, void *_cc, void *_tmo, int _slim, int *_msgidp);
extern int ldap_result(LDAP *_ld, int _msgid, int _all, void *_tmo, LDAPMessage **_res);
extern int ldap_msgfree(LDAPMessage *_msg);
extern int ldap_unbind_ext_s(LDAP *_ld, void *_sc, void *_cc);
struct c_ctx { const char *captured; };
static const char *c_capture(const struct c_ctx *c) { const char *_s = c->captured; while (*_s == ' ') _s++; return _s; }

void benchmark_test_00264(int argc, char **argv)
{
    (void)argc; (void)argv;
    char user_input_buf[256];
    user_input_buf[0] = '\0';
    if (fgets(user_input_buf, sizeof(user_input_buf), stdin) == NULL) user_input_buf[0] = '\0';
    user_input_buf[strcspn(user_input_buf, "\n")] = '\0';
    const char *user_input = user_input_buf;
    struct c_ctx _clx = { user_input };
    const char *data = c_capture(&_clx);
    LDAP *_ld = NULL;
    const char *_ldap_url = getenv("LDAP_URL");
    ldap_initialize(&_ld, _ldap_url != NULL ? _ldap_url : "ldap://directory:1389");
    int _ldap_version = LDAP_VERSION3;
    ldap_set_option(_ld, LDAP_OPT_PROTOCOL_VERSION, &_ldap_version);
    ldap_simple_bind_s(_ld, NULL, NULL);
    char _filter[512];
    snprintf(_filter, sizeof(_filter), "(mail=%s)", data);
    int _msgid = 0;
    ldap_search_ext(_ld, "ou=people,dc=example,dc=com", LDAP_SCOPE_SUBTREE, _filter, NULL, 0, NULL, NULL, NULL, 0, &_msgid);
    LDAPMessage *_res = NULL;
    if (ldap_result(_ld, _msgid, LDAP_MSG_ALL, NULL, &_res) > 0) ldap_msgfree(_res);
    ldap_unbind_ext_s(_ld, NULL, NULL);
}
