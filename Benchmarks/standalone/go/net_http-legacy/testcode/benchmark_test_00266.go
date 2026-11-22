// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/base64"
	"io/ioutil"
	"net/http"
)

func BenchmarkTest00266(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	decodedBytes, _ := base64.StdEncoding.DecodeString(cookieValue)
	data := string(decodedBytes)
	ioutil.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
