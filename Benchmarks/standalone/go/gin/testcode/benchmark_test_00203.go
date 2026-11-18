// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00203(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(dbValue)
	c.Redirect(http.StatusFound, data)
}
