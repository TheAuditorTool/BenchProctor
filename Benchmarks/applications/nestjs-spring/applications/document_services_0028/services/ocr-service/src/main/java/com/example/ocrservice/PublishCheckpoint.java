// SPDX-License-Identifier: Apache-2.0
package com.example.ocrservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class PublishCheckpoint {


    @GetMapping("/PublishCheckpoint")
    public void publishCheckpoint(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = authorization != null ? authorization : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String addendum = transform.apply(note);
        response.getWriter().print("<div>" + addendum + "</div>");
    }
}
