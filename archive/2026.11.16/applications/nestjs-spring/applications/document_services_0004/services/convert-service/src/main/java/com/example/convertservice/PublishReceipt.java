// SPDX-License-Identifier: Apache-2.0
package com.example.convertservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PublishReceipt {


    @GetMapping("/PublishReceipt")
    public void publishReceipt(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String excerpt = authorization != null ? authorization : "";
        String dossier;
        try { dossier = new String(java.util.Base64.getDecoder().decode(excerpt), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { dossier = excerpt; }
        response.getWriter().print("<div>" + dossier + "</div>");
    }
}
