// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"

	"github.com/gin-gonic/gin"
	"github.com/go-playground/validator/v10"
)

func BenchmarkTest00522(c *gin.Context) {
	userID := c.Query("id")
	validate := validator.New()
	validate.RegisterValidation("schema", func(fl validator.FieldLevel) bool {
		return regexp.MustCompile("^[a-zA-Z0-9 _.\\-]+$").MatchString(fl.Field().String())
	})
	if err := validate.Var(userID, "schema"); err != nil {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := userID
	c.Set("data", processed)
}
