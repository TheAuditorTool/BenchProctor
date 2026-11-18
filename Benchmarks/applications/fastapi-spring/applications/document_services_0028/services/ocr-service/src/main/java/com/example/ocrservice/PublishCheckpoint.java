// SPDX-License-Identifier: Apache-2.0
package com.example.ocrservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PublishCheckpoint {


    @GetMapping("/PublishCheckpoint")
    public void publishCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = authorization != null ? authorization : "";
        String addendum;
        try { addendum = new String(java.util.Base64.getDecoder().decode(note), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { addendum = note; }
        response.getWriter().print("<div>" + addendum + "</div>");
    }
}
