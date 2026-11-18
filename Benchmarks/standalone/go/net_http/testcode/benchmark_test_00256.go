// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00256(w http.ResponseWriter, r *http.Request) {
	fieldValue := r.FormValue("field")
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		http.Error(w, xmlErr.Error(), http.StatusInternalServerError)
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+fieldValue+"']")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
