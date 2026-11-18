// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"io"
	"net/http"
)

func BenchmarkTest00058(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	xmlBody := string(rawBytes)
	var data string
	if xmlBody != "" {
		data = xmlBody
	}
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
