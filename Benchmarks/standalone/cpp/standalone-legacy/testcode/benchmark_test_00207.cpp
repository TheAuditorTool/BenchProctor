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
struct berval { unsigned long bv_len; char *bv_val; };
extern "C" int ldap_compare_ext_s(LDAP *, const char *, const char *, struct berval *, void *, void *);
enum { LDAP_COMPARE_TRUE = 6 };

void benchmark_test_00207(int, char **)
{
    const char *user_input_env = std::getenv("HTTP_REFERER");
    std::string user_input = user_input_env ? std::string(user_input_env) : std::string();
    std::string data;
    switch (user_input.empty() ? '\0' : user_input[0]) {
        case '\0':
            data.clear();
            break;
        default:
            data = user_input;
            break;
    }
    LDAP *_ld = nullptr;
    const char *_ldap_url = std::getenv("LDAP_URL");
    ldap_initialize(&_ld, _ldap_url ? _ldap_url : "ldap://directory:1389");
    std::string _dn = std::string("uid=") + data + ",ou=people,dc=example,dc=com";
    struct berval _role = { 5, const_cast<char *>("admin") };
    int _rc = ldap_compare_ext_s(_ld, _dn.c_str(), "employeeType", &_role, nullptr, nullptr);
    std::cout << (_rc == LDAP_COMPARE_TRUE ? "admin" : "user") << std::endl;
    ldap_unbind_ext_s(_ld, nullptr, nullptr);
}
