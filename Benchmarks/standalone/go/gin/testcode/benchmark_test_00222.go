// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00222(c *gin.Context) {
	hostValue := c.Request.Host
	pending := strings.Split(hostValue, ",")
	var data string
	for len(pending) > 0 {
		data = pending[0]
		pending = pending[1:]
	}
	c.Redirect(http.StatusFound, data)
}
