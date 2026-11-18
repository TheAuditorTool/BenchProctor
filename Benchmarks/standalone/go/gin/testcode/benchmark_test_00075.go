// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io"
	"net/http"
	"regexp"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00075(c *gin.Context) {
	rawBytes, err := io.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	xmlBody := string(rawBytes)
	relayPrefix := ""
	if len(xmlBody) > 0 {
		relayPrefix = strings.ToLower(xmlBody[:1])
	}
	var data string
	switch relayPrefix {
	case "h":
		data = xmlBody
	case "f":
		data = xmlBody
	default:
		data = xmlBody
	}
	if !regexp.MustCompile("^(asc|desc|name|created)$").MatchString(data) {
		c.String(http.StatusBadRequest, "invalid option")
		return
	}
	processed := data
	c.Set("data", processed)
}
