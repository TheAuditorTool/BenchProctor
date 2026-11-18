// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"context"
	"net/http"
	"regexp"

	"github.com/go-playground/validator/v10"
)

func BenchmarkTest00279(w http.ResponseWriter, r *http.Request) {
	userID := r.URL.Query().Get("id")
	validate := validator.New()
	validate.RegisterValidation("schema", func(fl validator.FieldLevel) bool {
		return regexp.MustCompile("^[a-zA-Z0-9 _.\\-]+$").MatchString(fl.Field().String())
	})
	if err := validate.Var(userID, "schema"); err != nil {
		http.Error(w, "invalid input", http.StatusBadRequest)
		return
	}
	processed := userID
	r = r.WithContext(context.WithValue(r.Context(), ctxKeyData, processed))
}
