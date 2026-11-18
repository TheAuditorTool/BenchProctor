// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"strings"
)

func BenchmarkTest00051(w http.ResponseWriter, r *http.Request) {
	refererValue := r.Header.Get("Referer")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(refererValue)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
