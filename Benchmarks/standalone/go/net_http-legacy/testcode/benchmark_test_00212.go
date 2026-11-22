// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/sha512"
	"encoding/hex"
	"io"
	"io/ioutil"
	"net/http"
	"strings"
)

func BenchmarkTest00212(w http.ResponseWriter, r *http.Request) {
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
	digest := sha512.New()
	io.WriteString(digest, data)
	hashStr := hex.EncodeToString(digest.Sum(nil))
	RespondJSON(w, http.StatusOK, map[string]string{"hash": hashStr})
}
