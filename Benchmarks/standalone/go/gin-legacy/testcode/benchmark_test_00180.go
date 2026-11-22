// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"math/rand"
	"net/http"
	"strings"

	"github.com/gin-gonic/gin"
)

func BenchmarkTest00180(c *gin.Context) {
	userID := c.Query("id")
	segments := strings.Split(userID, ",")
	data := strings.Join(segments, " ")
	otpValue := rand.Int31n(1000000)
	otpCode := fmt.Sprintf("%06d", otpValue)
	DB.Exec("INSERT INTO login_challenges (account, code) VALUES ($1, $2)", data, otpCode)
	c.JSON(http.StatusOK, map[string]string{"status": "challenge_sent"})
}
