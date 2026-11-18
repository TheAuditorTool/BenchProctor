// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"strconv"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00045(c *gin.Context) {
	var dbValue string
	DB.QueryRow("SELECT name FROM users LIMIT 1").Scan(&dbValue)
	unpack := func(v string) (string, bool) { return v, v != "" }
	data, _ := unpack(dbValue)
	requested, _ := strconv.Atoi(data)
	wrapped := int32(requested + 1)
	c.Header("X-Wrapped", strconv.Itoa(int(wrapped)))
}
