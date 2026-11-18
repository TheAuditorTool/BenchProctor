// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"strconv"
	"strings"

	"github.com/go-ldap/ldap/v3"
)

func BenchmarkTest00077(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	segments := strings.Split(graphqlVar, ",")
	data := strings.Join(segments, " ")
	ldapConn, ldapErr := ldap.DialURL(envOr("LDAP_URL", "ldap://directory:1389"))
	if ldapErr != nil {
		http.Error(w, ldapErr.Error(), http.StatusInternalServerError)
		return
	}
	defer ldapConn.Close()
	searchReq := ldap.NewSearchRequest("ou=people,dc=example,dc=com", ldap.ScopeWholeSubtree, ldap.NeverDerefAliases, 0, 0, false, "(uid="+data+")", []string{"cn"}, nil)
	sr, _ := ldapConn.Search(searchReq)
	if sr != nil {
		w.Header().Set("X-LDAP-Count", strconv.Itoa(len(sr.Entries)))
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
