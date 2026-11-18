// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00124(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	data := strings.Join(strings.FieldsFunc(graphqlVar, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		http.Error(w, xmlErr.Error(), http.StatusInternalServerError)
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+data+"']")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
