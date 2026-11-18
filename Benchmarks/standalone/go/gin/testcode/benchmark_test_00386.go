// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"github.com/gin-gonic/gin"
	"github.com/microcosm-cc/bluemonday"
)

func BenchmarkTest00386(c *gin.Context) {
	fieldValue := c.PostForm("field")
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(fieldValue)
	processed := bluemonday.UGCPolicy().Sanitize(data)
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
