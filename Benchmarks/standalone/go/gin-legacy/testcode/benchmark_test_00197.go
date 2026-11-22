// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00197(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	allowed := map[string]bool{"config.json": true, "index.html": true, "readme.md": true}
	if !allowed[refererValue] {
		c.String(http.StatusForbidden, "forbidden")
		return
	}
	checkedPath := "/var/app/data/" + refererValue
	content, err := ioutil.ReadFile(checkedPath)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
