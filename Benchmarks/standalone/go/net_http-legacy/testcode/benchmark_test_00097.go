// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"bytes"
	"encoding/json"
	"html/template"
	"net/http"
	"strings"
)

func BenchmarkTest00097(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	var reqBody struct {
		Payload string `json:"payload"`
	}
	if err := json.NewDecoder(r.Body).Decode(&reqBody); err != nil {
		http.Error(w, "bad request", http.StatusBadRequest)
		return
	}
	jsonValue := reqBody.Payload
	data := strings.Join(strings.FieldsFunc(jsonValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	tmpl, _ := template.New("view").Parse("{{.}}")
	var buf bytes.Buffer
	tmpl.Execute(&buf, data)
	w.Write(buf.Bytes())
}
