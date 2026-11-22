// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00136(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	data := strings.ReplaceAll(headerValue, "\x00", "")
	content, err := ioutil.ReadFile("/var/app/data/" + data)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
