// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00462(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	segments := strings.Split(refererValue, ",")
	data := strings.Join(segments, " ")
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
