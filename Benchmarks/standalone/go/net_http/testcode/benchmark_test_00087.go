// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"regexp"
	"strings"

	"github.com/go-playground/validator/v10"
)

func BenchmarkTest00087(w http.ResponseWriter, r *http.Request) {
	cookieObj, err := r.Cookie("session_token")
	if err != nil {
		http.Error(w, "missing cookie", http.StatusBadRequest)
		return
	}
	cookieValue := cookieObj.Value
	data := func(v string) string { return strings.TrimSpace(v) }(cookieValue)
	validate := validator.New()
	validate.RegisterValidation("schema", func(fl validator.FieldLevel) bool {
		return regexp.MustCompile("^[a-zA-Z0-9 _.\\-]+$").MatchString(fl.Field().String())
	})
	if err := validate.Var(data, "schema"); err != nil {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := data
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, processed))
}
