// SPDX-License-Identifier: Apache-2.0
package com.example.trackingservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class LoadProfile {


    @GetMapping("/LoadProfile")
    public void loadProfile(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String subject = userAgent != null ? userAgent : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String parcel = transform.apply(subject);
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + parcel});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
