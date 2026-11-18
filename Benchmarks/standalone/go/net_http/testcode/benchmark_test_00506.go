// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"

	"github.com/yuin/goldmark"
)

func BenchmarkTest00506(w http.ResponseWriter, r *http.Request) {
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	var relayBuilder strings.Builder
	fmt.Fprintf(&relayBuilder, "%s", jsonValue)
	data := relayBuilder.String()
	var mdBuf bytes.Buffer
	goldmark.New().Convert([]byte(data), &mdBuf)
	processed := mdBuf.String()
	htmlOut := "<div>" + processed + "</div>"
	w.Write([]byte(htmlOut))
}
