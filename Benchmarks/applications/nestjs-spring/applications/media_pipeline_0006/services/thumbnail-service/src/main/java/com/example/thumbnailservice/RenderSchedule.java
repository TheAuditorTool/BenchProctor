// SPDX-License-Identifier: Apache-2.0
package com.example.thumbnailservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderSchedule {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/RenderSchedule", consumes="text/plain")
    public void renderSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String passage = rawBody != null ? rawBody : "";
        String montage = normalize(passage);
        if (!montage.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + montage + "</div>");
    }
}
