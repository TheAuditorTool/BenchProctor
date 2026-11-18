// SPDX-License-Identifier: Apache-2.0
package testcode

import (
	"net/http"
	"net/url"
	"strconv"

	"github.com/gin-gonic/gin"
	"github.com/go-ldap/ldap/v3"
)

func BenchmarkTest00048(c *gin.Context) {
	fieldValue := c.PostForm("field")
	data, _ := url.QueryUnescape(fieldValue)
	ldapConn, ldapErr := ldap.DialURL(envOr("LDAP_URL", "ldap://directory:1389"))
	if ldapErr != nil {
		c.String(http.StatusInternalServerError, ldapErr.Error())
		return
	}
	defer ldapConn.Close()
	searchReq := ldap.NewSearchRequest("ou=people,dc=example,dc=com", ldap.ScopeWholeSubtree, ldap.NeverDerefAliases, 0, 0, false, "(uid="+data+")", []string{"cn"}, nil)
	sr, _ := ldapConn.Search(searchReq)
	if sr != nil {
		c.Header("X-LDAP-Count", strconv.Itoa(len(sr.Entries)))
	}
	c.JSON(200, gin.H{"code": "OK"})
}
