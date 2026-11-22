// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"io/ioutil"
	"net/http"
)

func BenchmarkTest00003(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	rawBytes, err := ioutil.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	form := submissionForm{payload: rawBody}
	data := form.payload
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, data))
}
