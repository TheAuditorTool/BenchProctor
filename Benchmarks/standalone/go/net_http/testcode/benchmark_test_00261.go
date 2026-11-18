// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
)

func BenchmarkTest00261(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(authHeader)
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
