// SPDX-License-Identifier: Apache-2.0
package com.example.platformapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class VerifyDigest {


    @GetMapping("/VerifyDigest")
    public void verifyDigest(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = userAgent != null ? userAgent : "";
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", note);
        String handshake = sw.toString();
        response.getWriter().print("<div>" + handshake + "</div>");
    }
}
