// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00424(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	xmlBody := string(rawBytes)
	pending := strings.Split(xmlBody, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	validPattern := regexp.MustCompile("^[a-zA-Z0-9 _.\\-]+$")
	if !validPattern.MatchString(data) {
		c.String(http.StatusBadRequest, "invalid input")
		return
	}
	processed := data
	c.Set("data", processed)
}
