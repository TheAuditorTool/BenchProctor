// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"
)

func BenchmarkTest00338(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	hexBytes, _ := hex.DecodeString(authHeader)
	data := string(hexBytes)
	htmlOut := "<div>" + data + "</div>"
	w.Write([]byte(htmlOut))
}
