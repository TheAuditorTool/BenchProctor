// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00325(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	var data string
	for _, token := range strings.Split(refererValue, ",") {
		data = token
	}
	c.Redirect(http.StatusFound, data)
}
