// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00223(c *gin.Context) {
	multipartValue := c.PostForm("multipart_field")
	applyPolicy := func(v string) string { return strings.TrimSpace(v) }
	data := applyPolicy(multipartValue)
	c.Redirect(http.StatusFound, data)
}
