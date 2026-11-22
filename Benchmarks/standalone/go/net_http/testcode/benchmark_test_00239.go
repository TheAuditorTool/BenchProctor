// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"strconv"
	"strings"

	"github.com/go-ldap/ldap/v3"
)

func BenchmarkTest00239(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	relayPrefix := ""
	if len(graphqlVar) > 0 {
		relayPrefix = strings.ToLower(graphqlVar[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = graphqlVar
	case "f":
		data = graphqlVar
	default:
		data = graphqlVar
	}
	ldapConn, ldapErr := ldap.DialURL(envOr("LDAP_URL", "ldap://directory:1389"))
	if ldapErr != nil {
		http.Error(w, ldapErr.Error(), http.StatusInternalServerError)
		return
	}
	defer ldapConn.Close()
	directoryFilter := "(&(objectClass=inetOrgPerson)(mail=" + data + "))"
	pagedResult, searchErr := ldapConn.SearchWithPaging(ldap.NewSearchRequest("ou=people,dc=example,dc=com", ldap.ScopeWholeSubtree, ldap.NeverDerefAliases, 0, 0, false, directoryFilter, []string{"cn", "mail"}, nil), 50)
	if searchErr != nil {
		http.Error(w, searchErr.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("X-Directory-Matches", strconv.Itoa(len(pagedResult.Entries)))
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
