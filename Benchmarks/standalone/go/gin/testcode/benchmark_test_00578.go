// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00578(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(authHeader)
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
