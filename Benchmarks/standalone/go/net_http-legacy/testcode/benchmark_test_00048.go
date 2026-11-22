// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"io/ioutil"
	"net/http"
)

func BenchmarkTest00048(w http.ResponseWriter, r *http.Request) {
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
	data := string(bytes.TrimSpace([]byte(xmlBody)))
	trustedSettings.Store("partner_callback_host", data)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
