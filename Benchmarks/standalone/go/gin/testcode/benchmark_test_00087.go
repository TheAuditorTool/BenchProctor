// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00087(c *gin.Context) {
	userID := c.Query("id")
	data := strings.Join(strings.FieldsFunc(userID, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.\\-]+$")
	if !validPattern.MatchString(data) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	c.Set("data", processed)
}
