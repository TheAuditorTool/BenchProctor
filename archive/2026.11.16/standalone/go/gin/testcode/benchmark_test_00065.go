// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00065(c *gin.Context) {
	hostValue := c.Request.Host
	data := strings.ReplaceAll(hostValue, "\x00", "")
	c.Redirect(http.StatusFound, data)
}
