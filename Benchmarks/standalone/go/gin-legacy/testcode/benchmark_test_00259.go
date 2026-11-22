// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00259(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	var data string
	for _, token := range strings.Split(authHeader, ",") {
		data = token
	}
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	ioutil.WriteFile("/var/app/data/"+processed, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
