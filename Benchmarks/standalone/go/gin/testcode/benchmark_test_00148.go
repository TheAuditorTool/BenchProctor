// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00148(c *gin.Context) {
	pathValue := c.Param("id")
	var data string
	if pathValue != "" {
		data = pathValue
	}
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	os.WriteFile("/var/app/data/"+processed, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
