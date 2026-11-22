// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/base64"
	"io/ioutil"
	"net/http"
)

func BenchmarkTest00134(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	authHeader := r.Header.Get("Authorization")
	decodedBytes, _ := base64.StdEncoding.DecodeString(authHeader)
	data := string(decodedBytes)
	content, err := ioutil.ReadFile("/var/app/data/" + data)
	if err != nil {
		http.Error(w, "not found", http.StatusNotFound)
		return
	}
	w.Write(content)
}
