// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"fmt"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"github.com/go-ldap/ldap/v3"
)

func BenchmarkTest00144(c *gin.Context) {
	userID := c.Query("id")
	data := fmt.Sprintf("%s", userID)
	ldapConn, ldapErr := ldap.DialURL(envOr("LDAP_URL", "ldap://directory:1389"))
	if ldapErr != nil {
		c.String(http.StatusInternalServerError, ldapErr.Error())
		return
	}
	defer ldapConn.Close()
	isAdmin, cmpErr := ldapConn.Compare("uid="+data+",ou=people,dc=example,dc=com", "employeeType", "admin")
	if cmpErr != nil {
		c.String(http.StatusInternalServerError, cmpErr.Error())
		return
	}
	c.Header("X-Directory-Admin", strconv.FormatBool(isAdmin))
	c.JSON(200, gin.H{"code": "OK"})
}
