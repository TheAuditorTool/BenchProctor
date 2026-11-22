// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strconv"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/antchfx/xpath"
)

func BenchmarkTest00252(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
		return
	}
	authHeader := r.Header.Get("Authorization")
	var data string
	if len(authHeader) > 0 {
		data = authHeader
	} else {
		data = "default"
	}
	_lower := strings.ToLower(data)
	if !strings.HasPrefix(_lower, "t") && !strings.HasPrefix(_lower, "f") && _lower != "1" && _lower != "0" {
		http.Error(w, "invalid boolean", http.StatusBadRequest)
		return
	}
	parsedBool := strconv.FormatBool(strings.HasPrefix(_lower, "t") || _lower == "1")
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
	roleExpr, exprErr := xpath.Compile("//user[@name='" + parsedBool + "']/role")
	if exprErr != nil {
		http.Error(w, "invalid user name", http.StatusBadRequest)
		return
	}
	if roleNode := xmlquery.QuerySelector(xmlDoc, roleExpr); roleNode != nil {
		w.Header().Set("X-User-Role", roleNode.InnerText())
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
