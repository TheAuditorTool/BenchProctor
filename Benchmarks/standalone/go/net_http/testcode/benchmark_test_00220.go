// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"regexp"
	"strings"
)

func BenchmarkTest00220(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	data := strings.ReplaceAll(headerValue, "\x00", "")
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, processed))
}
