// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
)

func BenchmarkTest00297(w http.ResponseWriter, r *http.Request) {
	headerValue := r.Header.Get("X-Custom-Header")
	data := fmt.Sprintf("%s", headerValue)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
