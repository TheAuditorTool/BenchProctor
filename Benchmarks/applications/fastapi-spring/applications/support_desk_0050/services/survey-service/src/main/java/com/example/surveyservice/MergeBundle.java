// SPDX-License-Identifier: Apache-2.0
package com.example.surveyservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class MergeBundle {


    @GetMapping("/MergeBundle")
    public void mergeBundle(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = authorization != null ? authorization : "";
        String inquiry;
        try { inquiry = new String(java.util.Base64.getDecoder().decode(remark), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { inquiry = remark; }
        String grievance = inquiry.matches("^(status|info|list|show)$") ? inquiry : "status";
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + grievance}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
