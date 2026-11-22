// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00221(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(cookieValue)
	c.Redirect(http.StatusFound, data)
}
