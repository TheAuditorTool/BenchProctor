// SPDX-License-Identifier: Apache-2.0
package com.example.manifestbuilder;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ReconcileThreshold {


    @GetMapping("/ReconcileThreshold")
    public void reconcileThreshold(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String citation = authorization != null ? authorization : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : citation.split(",")) { tokens.add(token.trim()); }
        String parcel = String.join(",", tokens);
        new ProcessBuilder("echo", parcel).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
