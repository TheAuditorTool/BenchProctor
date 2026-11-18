// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
)

func BenchmarkTest00380(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	data := fmt.Sprintf("%s", authHeader)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
