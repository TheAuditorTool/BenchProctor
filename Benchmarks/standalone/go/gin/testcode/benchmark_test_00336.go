// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00336(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	capture := func() string { return strings.TrimSpace(headerValue) }
	data := capture()
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	c.Set("data", processed)
}
