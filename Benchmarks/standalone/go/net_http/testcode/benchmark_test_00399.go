// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"regexp"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00399(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	data, _ := url.QueryUnescape(fieldValue)
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.%~\\-]+$")
	if !validPattern.MatchString(data) {
		http.Error(w, "invalid input", http.StatusBadRequest)
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
