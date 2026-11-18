// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"os"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00178(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	capture := func() string { return strings.TrimSpace(multipartValue) }
	data := capture()
	content, err := os.ReadFile("/var/app/data/" + data)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
