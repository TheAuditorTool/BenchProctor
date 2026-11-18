// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00358(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	data := headerValue
	if _, after, ok := strings.Cut(headerValue, ","); ok {
		data = after
	}
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
