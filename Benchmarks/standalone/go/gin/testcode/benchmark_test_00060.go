// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00060(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	data := func(v string) string { return strings.TrimSpace(v) }(originValue)
	c.Redirect(http.StatusFound, data)
}
