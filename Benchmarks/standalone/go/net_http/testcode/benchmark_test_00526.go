// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"strings"
)

func BenchmarkTest00526(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	var data string
	for _, token := range strings.Split(originValue, ",") {
		data = token
	}
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
