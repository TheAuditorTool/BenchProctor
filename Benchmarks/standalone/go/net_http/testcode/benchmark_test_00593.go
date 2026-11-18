// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
)

func BenchmarkTest00593(w http.ResponseWriter, r *http.Request) {
	uaValue := r.Header.Get("User-Agent")
	data := fmt.Sprintf("%s", uaValue)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
