// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/go-playground/validator/v10"
)

func BenchmarkTest00057(w http.ResponseWriter, r *http.Request) {
	originValue := r.Header.Get("Origin")
	capture := func() string { return strings.TrimSpace(originValue) }
	data := capture()
	validate := validator.New()
	validate.RegisterValidation("schema", func(fl validator.FieldLevel) bool {
		return regexp.MustCompile("^[a-zA-Z0-9 _.%~\\-]+$").MatchString(fl.Field().String())
	})
	if err := validate.Var(data, "schema"); err != nil {
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
