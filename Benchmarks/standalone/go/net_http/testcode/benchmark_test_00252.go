// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"

	"github.com/antchfx/xmlquery"
	"github.com/antchfx/xpath"
)

func BenchmarkTest00252(w http.ResponseWriter, r *http.Request) {
	authHeader := r.Header.Get("Authorization")
	form := submissionForm{payload: authHeader}
	data := form.payload
	directoryFile, openErr := os.Open("/var/app/data/users.xml")
	if openErr != nil {
		http.Error(w, openErr.Error(), http.StatusInternalServerError)
		return
	}
	defer directoryFile.Close()
	xmlDoc, xmlErr := xmlquery.Parse(directoryFile)
	if xmlErr != nil {
		http.Error(w, xmlErr.Error(), http.StatusInternalServerError)
		return
	}
	roleExpr, exprErr := xpath.Compile("//user[@name='" + data + "']/role")
	if exprErr != nil {
		http.Error(w, "invalid user name", http.StatusBadRequest)
		return
	}
	if roleNode := xmlquery.QuerySelector(xmlDoc, roleExpr); roleNode != nil {
		w.Header().Set("X-User-Role", roleNode.InnerText())
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
