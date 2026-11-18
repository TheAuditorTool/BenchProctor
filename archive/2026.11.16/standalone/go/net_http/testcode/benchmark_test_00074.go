// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/base64"
	"io"
	"net/http"
)

func BenchmarkTest00074(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	rawBody := string(rawBytes)
	decodedBytes, _ := base64.StdEncoding.DecodeString(rawBody)
	data := string(decodedBytes)
	http.Redirect(w, r, data, http.StatusFound)
}
