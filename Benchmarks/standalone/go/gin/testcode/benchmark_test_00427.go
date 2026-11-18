// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strings"

	"github.com/antchfx/xmlquery"
	"github.com/gin-gonic/gin"
	"github.com/go-playground/validator/v10"
)

func BenchmarkTest00427(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	capture := func() string { return strings.TrimSpace(originValue) }
	data := capture()
	validate := validator.New()
	validate.RegisterValidation("schema", func(fl validator.FieldLevel) bool {
		return regexp.MustCompile("^[a-zA-Z0-9 _.%~\\-]+$").MatchString(fl.Field().String())
	})
	if err := validate.Var(data, "schema"); err != nil {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	xmlDoc, xmlErr := xmlquery.Parse(strings.NewReader("<root><user/></root>"))
	if xmlErr != nil {
		c.String(http.StatusInternalServerError, xmlErr.Error())
		return
	}
	xmlquery.FindOne(xmlDoc, "//user[@name='"+processed+"']")
	c.JSON(200, gin.H{"code": "OK"})
}
