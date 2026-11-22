// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00221(c *gin.Context) {
	fieldValue := c.PostForm("field")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(fieldValue)
	http.RedirectHandler(data, http.StatusFound).ServeHTTP(c.Writer, c.Request)
}
