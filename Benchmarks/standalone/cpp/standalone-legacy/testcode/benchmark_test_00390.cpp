// SPDX-License-Identifier: Apache-2.0
#include <iostream>
#include <string>
#include <cstdlib>

typedef struct ldap LDAP; typedef struct ldapmsg LDAPMessage;
extern "C" int ldap_initialize(LDAP **, const char *);
extern "C" int ldap_search_ext_s(LDAP *, const char *, int, const char *, char **, int, void *, void *, void *, int, LDAPMessage **);
extern "C" int ldap_msgfree(LDAPMessage *);
extern "C" int ldap_unbind_ext_s(LDAP *, void *, void *);
enum { LDAP_SCOPE_SUBTREE = 2 };
extern "C" int ldap_search_ext(LDAP *, const char *, int, const char *, char **, int, void *, void *, void *, int, int *);
extern "C" int ldap_result(LDAP *, int, int, void *, LDAPMessage **);
enum { LDAP_MSG_ALL = 1 };

void benchmark_test_00390(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_HOST");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    LDAP *_ld = nullptr;
    const char *_ldap_url = std::getenv("LDAP_URL");
    ldap_initialize(&_ld, _ldap_url ? _ldap_url : "ldap://directory:1389");
    std::string _filter = std::string("(mail=") + user_input + ")";
    int _msgid = 0;
    ldap_search_ext(_ld, "dc=example,dc=com", LDAP_SCOPE_SUBTREE, _filter.c_str(), nullptr, 0, nullptr, nullptr, nullptr, 0, &_msgid);
    LDAPMessage *_lres = nullptr;
    if (ldap_result(_ld, _msgid, LDAP_MSG_ALL, nullptr, &_lres) > 0) ldap_msgfree(_lres);
    ldap_unbind_ext_s(_ld, nullptr, nullptr);
}
