// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/hex"
	"net/http"
	"regexp"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00374(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	hexBytes, _ := hex.DecodeString(cookieValue)
	data := string(hexBytes)
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
