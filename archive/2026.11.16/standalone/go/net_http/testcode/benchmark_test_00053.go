// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strings"
)

func BenchmarkTest00053(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", uaValue)
	data := relayBuilder.String()
	http.SetCookie(w, &http.Cookie{Name: "session", Value: data, HttpOnly: true, SameSite: http.SameSiteStrictMode})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
