// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
)

func BenchmarkTest00306(w http.ResponseWriter, r *http.Request) {
	forwardedIP := r.Header.Get("X-Forwarded-For")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(forwardedIP)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
