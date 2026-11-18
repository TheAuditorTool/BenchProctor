// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00377(c *gin.Context) {
	forwardedIP := c.GetHeader("X-Forwarded-For")
	pending := strings.Split(forwardedIP, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", data)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	if result == nil {
		c.String(404, "not found")
		return
	}
	c.JSON(http.StatusOK, map[string]string{"name": *result})
}
