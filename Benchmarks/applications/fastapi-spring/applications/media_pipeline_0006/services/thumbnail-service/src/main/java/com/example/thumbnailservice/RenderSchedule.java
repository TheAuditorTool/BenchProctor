// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderSchedule {


    @GetMapping("/RenderSchedule")
    public void renderSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(passage, "body");
        String montage = tuple.getKey();
        if (!montage.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + montage + "</div>");
    }
}
