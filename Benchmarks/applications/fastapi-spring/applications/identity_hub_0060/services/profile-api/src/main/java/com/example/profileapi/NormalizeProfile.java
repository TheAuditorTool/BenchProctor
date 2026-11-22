// SPDX-License-Identifier: Apache-2.0
package com.example.profileapi;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class NormalizeProfile {


    @PostMapping(path="/NormalizeProfile", consumes="text/plain")
    public void normalizeProfile(@javax.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = rawBody != null ? rawBody : "";
        byte[] raw = paragraph.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String persona = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        String blurb = persona.matches("^(plain|markdown|html|text)$") ? persona : "plain";
        response.getWriter().print("<div>" + blurb + "</div>");
    }
}
