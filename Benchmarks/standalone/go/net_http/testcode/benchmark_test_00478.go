// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
)

func BenchmarkTest00478(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(refererValue)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
