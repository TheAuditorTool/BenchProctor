// SPDX-License-Identifier: Apache-2.0
package com.example.orderhistory;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FetchRoster {


    @GetMapping("/FetchRoster")
    public void fetchRoster(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String heading = id != null ? id : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : heading.split(",")) { tokens.add(token.trim()); }
        String voucher = String.join(",", tokens);
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + voucher});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
