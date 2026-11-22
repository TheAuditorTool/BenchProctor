// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00211(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	var data string
	for _, token := range strings.Split(forwardedIP, ",") {
		data = token
	}
	allowed := map[string]bool{"config.json": true, "index.html": true, "readme.md": true}
	if !allowed[data] {
		c.String(http.StatusForbidden, "forbidden")
		return
	}
	checkedPath := "/var/app/data/" + data
	ioutil.WriteFile(checkedPath, []byte("data"), 0644)
	c.JSON(200, gin.H{"code": "OK"})
}
