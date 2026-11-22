// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"encoding/base64"
	"io/ioutil"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00057(c *gin.Context) {
	authHeader := c.GetHeader("Authorization")
	decodedBytes, _ := base64.StdEncoding.DecodeString(authHeader)
	data := string(decodedBytes)
	content, err := ioutil.ReadFile("/var/app/data/" + data)
	if err != nil {
		c.String(http.StatusNotFound, "not found")
		return
	}
	c.Data(200, "text/plain", content)
}
