// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00122(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	multipartValue := r.FormValue("multipart_field")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", multipartValue)
	data := relayBuilder.String()
	sessionCookie := &http.Cookie{Name: "session", Value: data, Path: "/", HttpOnly: true, SameSite: http.SameSiteStrictMode}
	w.Header().Add("Set-Cookie", sessionCookie.String())
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
