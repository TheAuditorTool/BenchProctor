// SPDX-License-Identifier: Apache-2.0
package com.example.bridgeservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RotateBatch {


    @GetMapping("/RotateBatch")
    public void rotateBatch(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = userAgent != null ? userAgent : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String handshake = transform.apply(preface);
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + handshake});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
