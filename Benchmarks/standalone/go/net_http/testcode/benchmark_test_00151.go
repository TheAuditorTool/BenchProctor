// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/json"
	"net/http"
	"regexp"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00151(w http.ResponseWriter, r *http.Request) {
	var gqlReq struct {
		Variables map[string]string `json:"variables"`
	}
	json.NewDecoder(r.Body).Decode(&gqlReq)
	graphqlVar := gqlReq.Variables["input"]
	data := strings.Join(strings.FieldsFunc(graphqlVar, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		http.Error(w, "invalid option", http.StatusBadRequest)
		return
	}
	processed := data
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		http.Error(w, xmlErr.Error(), http.StatusInternalServerError)
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+processed+"']")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
