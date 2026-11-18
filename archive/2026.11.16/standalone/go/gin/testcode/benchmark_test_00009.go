// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00009(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	var data string
	if len(authHeader) > 0 {
		data = authHeader
	} else {
		data = "default"
	}
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.\\-]+$")
	if !validPattern.MatchString(data) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	c.Set("data", processed)
}
