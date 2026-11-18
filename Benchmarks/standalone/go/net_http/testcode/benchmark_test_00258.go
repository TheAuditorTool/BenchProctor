// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00258(w http.ResponseWriter, r *http.Request) {
	pathValue := strings.TrimPrefix(r.URL.Path, "/api/")
	form := submissionForm{payload: pathValue}
	data := form.payload
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
