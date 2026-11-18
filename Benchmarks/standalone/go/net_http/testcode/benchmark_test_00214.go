// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
)

func BenchmarkTest00214(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	http.SetCookie(w, &http.Cookie{Name: "session", Value: userID, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
