// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"html"
	"net/http"
	"strings"
)

func BenchmarkTest00345(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(cookieValue)
	processed := html.EscapeString(data)
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
