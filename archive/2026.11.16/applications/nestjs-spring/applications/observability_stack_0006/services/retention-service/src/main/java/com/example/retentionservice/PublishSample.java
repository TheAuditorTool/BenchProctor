// SPDX-License-Identifier: Apache-2.0
package com.example.retentionservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PublishSample {


    @GetMapping("/PublishSample")
    public void publishSample(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = authorization != null ? authorization : "";
        String cohort;
        try { cohort = new String(java.util.Base64.getDecoder().decode(preface), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { cohort = preface; }
        response.getWriter().print("<div>" + cohort + "</div>");
    }
}
