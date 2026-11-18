// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00242(c *gin.Context) {
	hostValue := c.Request.Host
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(hostValue) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := hostValue
	os.Remove("/var/app/data/" + processed)
	c.JSON(200, gin.H{"code": "OK"})
}
