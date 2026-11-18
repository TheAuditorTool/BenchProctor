// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00006(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	var data string
	for _, token := range strings.Split(rawBody, ",") {
		data = token
	}
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.\\-]+$")
	if !validPattern.MatchString(data) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	c.Set("data", processed)
}
