// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strconv"
	"strings"

	"github.com/go-ldap/ldap/v3"
)

func BenchmarkTest00095(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	capture := func() string { return strings.TrimSpace(uaValue) }
	data := capture()
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	ldapConn, ldapErr := ldap.DialURL(envOr("LDAP_URL", "ldap://directory:1389"))
	if ldapErr != nil {
		http.Error(w, ldapErr.Error(), http.StatusInternalServerError)
		return
	}
	defer ldapConn.Close()
	directoryFilter := "(&(objectClass=inetOrgPerson)(mail=" + processed + "))"
	pagedResult, searchErr := ldapConn.SearchWithPaging(ldap.NewSearchRequest("ou=people,dc=example,dc=com", ldap.ScopeWholeSubtree, ldap.NeverDerefAliases, 0, 0, false, directoryFilter, []string{"cn", "mail"}, nil), 50)
	if searchErr != nil {
		http.Error(w, searchErr.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("X-Directory-Matches", strconv.Itoa(len(pagedResult.Entries)))
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
