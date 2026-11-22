// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand"
	"net/http"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00022(c *gin.Context) {
	uaValue := c.GetHeader("User-Agent")
	otpValue := rand.Int31n(1000000)
	otpCode := fmt.Sprintf("%06d", otpValue)
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", uaValue, otpCode)
	c.JSON(http.StatusOK, map[string]string{"status": "challenge_sent"})
}
