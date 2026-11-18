// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"net/http"
	"net/url"

	"github.com/yuin/goldmark"
)

func BenchmarkTest00451(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	data, _ := url.QueryUnescape(cookieValue)
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
