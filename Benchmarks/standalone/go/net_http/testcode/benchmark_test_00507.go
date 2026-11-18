// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00507(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	data := func(v string) string { return strings.TrimSpace(v) }(rawBody)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
