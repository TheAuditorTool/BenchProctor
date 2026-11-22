// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"
	"strconv"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00028(w http.ResponseWriter, r *http.Request) {
	forwardedIP := r.Header.Get("X-Forwarded-For")
	data := strings.Join(strings.FieldsFunc(forwardedIP, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.%~\\-]+$")
	if !validPattern.MatchString(data) {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	directoryFile, openErr := os.Open("/var/app/data/users.xml")
	if openErr != nil {
		http.Error(w, openErr.Error(), http.StatusInternalServerError)
		return
	}
	defer directoryFile.Close()
	xmlDoc, xmlErr := xmlquery.Parse(directoryFile)
	if xmlErr != nil {
		http.Error(w, xmlErr.Error(), http.StatusInternalServerError)
		return
	}
	userNodes, queryErr := xmlquery.QueryAll(xmlDoc, "//user[@name='"+processed+"']")
	if queryErr != nil {
		http.Error(w, "invalid user name", http.StatusBadRequest)
		return
	}
	w.Header().Set("X-User-Matches", strconv.Itoa(len(userNodes)))
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
