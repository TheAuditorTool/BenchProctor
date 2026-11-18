// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"strings"
)

func BenchmarkTest00518(w http.ResponseWriter, r *http.Request) {
	rawBytes, err := io.ReadAll(r.Body)
	if err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	xmlBody := string(rawBytes)
	relayPrefix := ""
	if len(xmlBody) > 0 {
		relayPrefix = strings.ToLower(xmlBody[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = xmlBody
	case "f":
		data = xmlBody
	default:
		data = xmlBody
	}
	http.Redirect(w, r, data, http.StatusFound)
}
