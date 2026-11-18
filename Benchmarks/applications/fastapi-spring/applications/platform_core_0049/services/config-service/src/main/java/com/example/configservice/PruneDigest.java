// SPDX-License-Identifier: Apache-2.0
package com.example.configservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PruneDigest {


    @GetMapping("/PruneDigest")
    public void pruneDigest(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = authorization != null ? authorization : "";
        String persona;
        if (notice.length() > 256) { persona = notice.substring(0, 256); }
        else { persona = notice; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + persona}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
