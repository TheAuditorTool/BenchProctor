// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00363(w http.ResponseWriter, r *http.Request) {
	multipartValue := r.FormValue("multipart_field")
	capture := func() string { return strings.TrimSpace(multipartValue) }
	data := capture()
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
