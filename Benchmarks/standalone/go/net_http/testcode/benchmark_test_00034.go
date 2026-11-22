// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"

	"github.com/antchfx/xmlquery"
	"github.com/antchfx/xpath"
	"github.com/go-playground/validator/v10"
)

func BenchmarkTest00034(w http.ResponseWriter, r *http.Request) {
	var commentText string
	DB.QueryRow("SELECT text FROM comments LIMIT 1").Scan(&commentText)
	var data string
	if len(commentText) > 0 {
		data = commentText
	} else {
		data = "default"
	}
	validate := validator.New()
	validate.RegisterValidation("schema", func(fl validator.FieldLevel) bool {
		return regexp.MustCompile("^[a-zA-Z0-9 _.%~\\-]+$").MatchString(fl.Field().String())
	})
	if err := validate.Var(data, "schema"); err != nil {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
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
	roleExpr, exprErr := xpath.Compile("//user[@name='" + processed + "']/role")
	if exprErr != nil {
		http.Error(w, "invalid user name", http.StatusBadRequest)
		return
	}
	if roleNode := xmlquery.QuerySelector(xmlDoc, roleExpr); roleNode != nil {
		w.Header().Set("X-User-Role", roleNode.InnerText())
	}
	RespondJSON(w, http.StatusOK, map[string]string{"state": "active"})
}
