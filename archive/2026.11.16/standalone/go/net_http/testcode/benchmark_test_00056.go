// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"
	"strings"

	"github.com/antchfx/xmlquery"
)

func BenchmarkTest00056(w http.ResponseWriter, r *http.Request) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	data := fmt.Sprintf("%s", commentText)
	_lower := strings.ToLower(data)
	if !strings.HasPrefix(_lower, "t") && !strings.HasPrefix(_lower, "f") && _lower != "1" && _lower != "0" {
		http.Error(w, "invalid boolean", http.StatusBadRequest)
		return
	}
	parsedBool := strconv.FormatBool(strings.HasPrefix(_lower, "t") || _lower == "1")
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		http.Error(w, xmlErr.Error(), http.StatusInternalServerError)
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+parsedBool+"']")
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
