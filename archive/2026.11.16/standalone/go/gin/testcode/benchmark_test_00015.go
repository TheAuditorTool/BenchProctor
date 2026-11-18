// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00015(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	data := func(v string) string { return strings.TrimSpace(v) }(forwardedIP)
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", data)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	c.JSON(http.StatusOK, map[string]string{"name": *result})
}
