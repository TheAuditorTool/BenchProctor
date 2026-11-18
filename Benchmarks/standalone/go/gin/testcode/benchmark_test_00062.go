// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00062(c *gin.Context) {
	pathValue := c.Param("id")
	data := pathValue
	if _, after, ok := strings.Cut(pathValue, ","); ok {
		data = after
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
