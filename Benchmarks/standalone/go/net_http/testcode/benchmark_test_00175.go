// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strings"
)

func BenchmarkTest00175(w http.ResponseWriter, r *http.Request) {
	pathValue := strings.TrimPrefix(r.URL.Path, "/api/")
	data := strings.Join(strings.FieldsFunc(pathValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.#%\\-]+$")
	if !validPattern.MatchString(data) {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
