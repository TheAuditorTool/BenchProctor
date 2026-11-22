// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"io/ioutil"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00116(c *gin.Context) {
	rawBytes, err := ioutil.ReadAll(c.Request.Body)
	if err != nil {
		c.String(http.StatusBadRequest, "bad request")
		return
	}
	rawBody := string(rawBytes)
	data := strings.ReplaceAll(rawBody, "\x00", "")
	c.Redirect(http.StatusFound, data)
}
