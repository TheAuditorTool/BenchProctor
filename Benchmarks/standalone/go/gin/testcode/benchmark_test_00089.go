// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strings"

	"github.com/gin-gonic/gin"
	"github.com/microcosm-cc/bluemonday"
)

func BenchmarkTest00089(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	data := func(v string) string { return strings.TrimSpace(v) }(dbValue)
	processed := bluemonday.UGCPolicy().Sanitize(data)
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
