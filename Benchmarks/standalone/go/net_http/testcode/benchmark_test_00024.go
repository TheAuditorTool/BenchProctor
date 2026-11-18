// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
)

func BenchmarkTest00024(w http.ResponseWriter, r *http.Request) {
	forwardedIP := r.Header.Get("X-Forwarded-For")
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, forwardedIP))
}
