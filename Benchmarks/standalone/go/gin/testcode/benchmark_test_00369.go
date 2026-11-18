// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00369(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	var result *string
	row := DB.QueryRow("SELECT name FROM users WHERE id = $1", uaValue)
	var name string
	if scanErr := row.Scan(&name); scanErr == nil {
		result = &name
	}
	c.JSON(http.StatusOK, map[string]string{"name": *result})
}
