// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00050(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	capture := func() string { return strings.TrimSpace(dbValue) }
	data := capture()
	c.Header("Content-Type", "text/html; charset=utf-8")
	fmt.Fprintf(c.Writer, "<p>Results for %s</p>", data)
}
