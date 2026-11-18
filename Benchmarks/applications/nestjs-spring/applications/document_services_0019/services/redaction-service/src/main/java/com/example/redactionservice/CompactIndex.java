// SPDX-License-Identifier: Apache-2.0
package com.example.redactionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CompactIndex {


    @GetMapping("/CompactIndex")
    public void compactIndex(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = userAgent != null ? userAgent : "";
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", passage);
        String dossier = sw.toString();
        response.getWriter().print("<div>" + dossier + "</div>");
    }
}
