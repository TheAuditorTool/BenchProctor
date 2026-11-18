// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"regexp"
	"strings"
)

func BenchmarkTest00542(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	capture := func() string { return strings.TrimSpace(headerValue) }
	data := capture()
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, processed))
}
