// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00013(c *gin.Context) {
	hostValue := c.Request.Host
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(hostValue)
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	c.Set("data", processed)
}
