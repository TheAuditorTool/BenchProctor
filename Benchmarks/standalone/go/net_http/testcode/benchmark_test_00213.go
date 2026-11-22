// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"regexp"
	"strings"
)

func BenchmarkTest00213(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	data := func(v string) string { return strings.TrimSpace(v) }(cookieValue)
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.\\-]+$")
	if !validPattern.MatchString(data) {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	redisClient.HSet(context.Background(), "session:"+ctxString(r, ctxKeyUser), map[string]any{"display_name": processed, "locale": "en"})
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
