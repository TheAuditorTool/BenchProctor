// SPDX-License-Identifier: Apache-2.0
package com.example.dashboardapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class BuildThreshold {


    @GetMapping("/BuildThreshold")
    public void buildThreshold(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = authorization != null ? authorization : "";
        String cohort;
        if (headline.length() > 256) { cohort = headline.substring(0, 256); }
        else { cohort = headline; }
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + cohort}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
