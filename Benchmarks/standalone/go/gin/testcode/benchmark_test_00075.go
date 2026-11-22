// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00075(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	data := strings.Join(strings.FieldsFunc(uaValue, func(r rune) bool { return r == ' ' || r == '\t' }), " ")
	apiToken := rand.Text()
	DB.Exec("INSERT INTO api_tokens (label, token) VALUES ($1, $2)", data, apiToken)
	c.JSON(http.StatusOK, map[string]string{"token": apiToken})
}
