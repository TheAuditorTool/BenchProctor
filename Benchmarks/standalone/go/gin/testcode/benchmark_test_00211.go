// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"os"
	"regexp"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00211(c *gin.Context) {
	userID := c.Query("id")
	data, _ := url.QueryUnescape(userID)
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	os.WriteFile("/var/app/data/"+processed, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
