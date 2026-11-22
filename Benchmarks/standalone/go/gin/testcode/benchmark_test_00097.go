// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00097(c *gin.Context) {
	refererValue := c.GetHeader("Referer")
	data := fmt.Sprintf("%s", refererValue)
	c.Header("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(c.Writer, "<p>Results for %s</p>", data)
}
