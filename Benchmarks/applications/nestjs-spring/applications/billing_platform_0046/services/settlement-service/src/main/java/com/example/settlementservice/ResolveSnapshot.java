// SPDX-License-Identifier: Apache-2.0
package com.example.settlementservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ResolveSnapshot {


    @GetMapping("/ResolveSnapshot")
    public void resolveSnapshot(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = id != null ? id : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : remark.split(",")) { tokens.add(token.trim()); }
        String remittance = String.join(",", tokens);
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + remittance});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
