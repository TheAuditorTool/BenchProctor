// SPDX-License-Identifier: Apache-2.0
package com.example.cartservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class RotateProfile {


    @GetMapping("/RotateProfile")
    public void rotateProfile(@javax.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headline = userAgent != null ? userAgent : "";
        java.util.function.Supplier<String> valueSupplier = () -> headline.strip();
        String backorder = valueSupplier.get();
        Runtime.getRuntime().exec(new String[]{"sh", "-c", "echo " + backorder}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
