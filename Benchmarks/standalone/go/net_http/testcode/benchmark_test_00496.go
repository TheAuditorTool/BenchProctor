// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00496(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	var data string
	if refererValue != "" {
		data = refererValue
	}
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
