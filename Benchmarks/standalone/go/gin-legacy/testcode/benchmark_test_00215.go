// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00215(c *gin.Context) {
	originValue := c.GetHeader("Origin")
	segments := strings.Split(originValue, ",")
	data := strings.Join(segments, " ")
	c.Header("Location", data)
	c.Status(http.StatusSeeOther)
}
