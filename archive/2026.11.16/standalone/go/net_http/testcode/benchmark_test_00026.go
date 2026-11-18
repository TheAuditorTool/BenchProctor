// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00026(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	data := func(v string) string { return strings.TrimSpace(v) }(uaValue)
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
