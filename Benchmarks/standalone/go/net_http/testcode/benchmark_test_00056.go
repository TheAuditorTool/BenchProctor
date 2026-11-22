// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"strings"
)

func BenchmarkTest00056(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	segments := strings.Split(uaValue, ",")
	data := strings.Join(segments, " ")
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
