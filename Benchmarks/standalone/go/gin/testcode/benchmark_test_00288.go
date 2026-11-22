// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"crypto/rand"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00288(c *gin.Context) {
	headerValue := c.GetHeader("X-Custom-Header")
	form := submissionForm{payload: headerValue}
	data := form.payload
	apiToken := rand.Text()
	DB.Exec("INSERT INTO api_tokens (label, token) VALUES ($1, $2)", data, apiToken)
	c.JSON(http.StatusOK, map[string]string{"token": apiToken})
}
