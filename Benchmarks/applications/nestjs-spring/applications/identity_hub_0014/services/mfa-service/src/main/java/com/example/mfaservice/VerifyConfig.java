// SPDX-License-Identifier: Apache-2.0
package com.example.mfaservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class VerifyConfig {


    @GetMapping("/VerifyConfig")
    public void verifyConfig(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = authorization != null ? authorization : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String persona = transform.apply(snippet);
        response.getWriter().print("<div>" + persona + "</div>");
    }
}
