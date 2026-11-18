// SPDX-License-Identifier: Apache-2.0
package com.example.surveyservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FetchHeader {


    @GetMapping("/FetchHeader")
    public void fetchHeader(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String remark = java.util.Optional.ofNullable(System.getenv("SUPPORT_INPUT_0050")).orElse("");
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(remark, "form");
        String inquiry = pair.getKey();
        new ProcessBuilder("echo", inquiry).start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
