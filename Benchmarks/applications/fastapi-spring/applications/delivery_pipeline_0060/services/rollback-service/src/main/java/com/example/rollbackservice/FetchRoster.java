// SPDX-License-Identifier: Apache-2.0
package com.example.rollbackservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FetchRoster {


    @GetMapping("/FetchRoster")
    public void fetchRoster(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String wording = java.util.Optional.ofNullable(System.getenv("DELIVERY_INPUT_0060")).orElse("");
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(wording, "header");
        String remark = pair.getKey();
        new ProcessBuilder("echo", remark).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
