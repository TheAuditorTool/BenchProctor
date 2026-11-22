// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"
	"strings"
)

func BenchmarkTest00077(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	originValue := r.Header.Get("Origin")
	data := originValue
	if _, after, ok := strings.Cut(originValue, ","); ok {
		data = after
	}
	ioutil.WriteFile("/var/app/data/"+data, []byte("data"), 0644)
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
