// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class MergeIndex {


    @GetMapping("/MergeIndex")
    public void mergeIndex(@javax.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String blurb = xForwardedFor != null ? xForwardedFor : "";
        String inquiry = blurb.isEmpty() ? "default" : blurb;
        if (!inquiry.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + inquiry + "</div>");
    }
}
