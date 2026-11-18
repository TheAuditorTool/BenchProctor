// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"

	"github.com/gin-gonic/gin"
	"github.com/microcosm-cc/bluemonday"
)

func BenchmarkTest00449(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	data := fmt.Sprintf("%s", dbValue)
	processed := bluemonday.UGCPolicy().Sanitize(data)
	htmlOut := "<div>" + processed + "</div>"
	c.Data(200, "text/html", []byte(htmlOut))
}
