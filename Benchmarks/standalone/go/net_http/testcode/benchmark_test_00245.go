// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strconv"
	"strings"

	"github.com/go-ldap/ldap/v3"
	"github.com/go-playground/validator/v10"
)

func BenchmarkTest00245(w http.ResponseWriter, r *http.Request) {
	_, header, err := r.FormFile("upload")
	if err != nil {
		http.Error(w, "bad upload", http.StatusBadRequest)
		return
	}
	uploadName := header.Filename
	data := uploadName
	if _, after, ok := strings.Cut(uploadName, ","); ok {
		data = after
	}
	validate := validator.New()
	validate.RegisterValidation("schema", func(fl validator.FieldLevel) bool {
		return regexp.MustCompile("^[a-zA-Z0-9 _.#%\\-]+$").MatchString(fl.Field().String())
	})
	if err := validate.Var(data, "schema"); err != nil {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	ldapConn, ldapErr := ldap.DialURL(envOr("LDAP_URL", "ldap://directory:1389"))
	if ldapErr != nil {
		http.Error(w, ldapErr.Error(), http.StatusInternalServerError)
		return
	}
	defer ldapConn.Close()
	searchReq := ldap.NewSearchRequest("ou=people,dc=example,dc=com", ldap.ScopeWholeSubtree, ldap.NeverDerefAliases, 0, 0, false, "(uid="+processed+")", []string{"cn"}, nil)
	sr, _ := ldapConn.Search(searchReq)
	if sr != nil {
		w.Header().Set("X-LDAP-Count", strconv.Itoa(len(sr.Entries)))
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
