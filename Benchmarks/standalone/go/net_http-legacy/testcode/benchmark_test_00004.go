// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func BenchmarkTest00004(w http.ResponseWriter, r *http.Request) {
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
	data := fmt.Sprintf("%s", rawBody)
	http.RedirectHandler(data, http.StatusFound).ServeHTTP(w, r)
}
