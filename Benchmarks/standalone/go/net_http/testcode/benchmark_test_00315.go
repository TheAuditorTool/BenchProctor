// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"
)

func BenchmarkTest00315(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	data := userID
	if _, after, ok := strings.Cut(userID, ","); ok {
		data = after
	}
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, Secure: true, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
