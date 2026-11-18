// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"fmt"
	"net/http"
)

func BenchmarkTest00266(w http.ResponseWriter, r *http.Request) {
	hostValue := r.Host
	data := fmt.Sprintf("%s", hostValue)
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
