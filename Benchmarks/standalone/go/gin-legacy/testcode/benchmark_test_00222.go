// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00222(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	pending := strings.Split(headerValue, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	http.RedirectHandler(data, http.StatusFound).ServeHTTP(c.Writer, c.Request)
}
