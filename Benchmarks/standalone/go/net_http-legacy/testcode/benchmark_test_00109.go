// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"io/ioutil"
	"net/http"
	"strings"
)

func BenchmarkTest00109(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	rawBytes, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	xmlBody := string(rawBytes)
	segments := strings.Split(xmlBody, ",")
	data := strings.Join(segments, " ")
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
