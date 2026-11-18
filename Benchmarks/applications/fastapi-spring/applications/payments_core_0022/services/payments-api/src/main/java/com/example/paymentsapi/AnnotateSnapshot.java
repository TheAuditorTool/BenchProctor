// SPDX-License-Identifier: Apache-2.0
package com.example.paymentsapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class AnnotateSnapshot {


    @GetMapping("/AnnotateSnapshot")
    public void annotateSnapshot(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = authorization != null ? authorization : "";
        String ledger;
        if (subject.length() > 256) { ledger = subject.substring(0, 256); }
        else { ledger = subject; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + ledger}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
