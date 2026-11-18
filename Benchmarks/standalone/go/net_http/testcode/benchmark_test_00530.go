// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
)

func BenchmarkTest00530(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	var data string
	if uaValue != "" {
		data = uaValue
	}
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
