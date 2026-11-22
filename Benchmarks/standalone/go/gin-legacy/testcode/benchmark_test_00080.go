// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00080(c *gin.Context) {
	cookieValue, err := c.Cookie("session_token")
	if err != nil {
		c.String(http.StatusBadRequest, "missing cookie")
		return
	}
	segments := strings.Split(cookieValue, ",")
	data := strings.Join(segments, " ")
	http.RedirectHandler(data, http.StatusFound).ServeHTTP(c.Writer, c.Request)
}
