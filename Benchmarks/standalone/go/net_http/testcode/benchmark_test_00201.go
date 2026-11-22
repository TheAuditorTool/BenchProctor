// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"regexp"
	"strings"
)

func BenchmarkTest00201(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	data := strings.Join(strings.FieldsFunc(userID, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.\\-]+$")
	if !validPattern.MatchString(data) {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, processed))
}
