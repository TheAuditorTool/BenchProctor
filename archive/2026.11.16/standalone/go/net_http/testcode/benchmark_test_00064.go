// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"regexp"
)

func BenchmarkTest00064(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	var data string
	if len(authHeader) > 0 {
		data = authHeader
	} else {
		data = "default"
	}
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.\\-]+$")
	if !validPattern.MatchString(data) {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, processed))
}
