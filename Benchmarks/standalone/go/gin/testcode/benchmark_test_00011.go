// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/url"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00011(c *gin.Context) {
	userID := c.Query("id")
	data, _ := url.QueryUnescape(userID)
	c.Header("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(c.Writer, "<p>Results for %s</p>", data)
}
