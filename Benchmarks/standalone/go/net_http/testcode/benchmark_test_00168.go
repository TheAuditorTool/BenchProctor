// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"strings"
)

func BenchmarkTest00168(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	capture := func() string { return strings.TrimSpace(originValue) }
	data := capture()
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
