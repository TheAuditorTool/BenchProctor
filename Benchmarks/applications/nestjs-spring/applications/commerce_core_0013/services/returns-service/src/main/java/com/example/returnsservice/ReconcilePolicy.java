// SPDX-License-Identifier: Apache-2.0
package com.example.returnsservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ReconcilePolicy {


    @GetMapping("/ReconcilePolicy")
    public void reconcilePolicy(@javax.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String wording = xForwardedFor != null ? xForwardedFor : "";
        String backorder = wording.isEmpty() ? "default" : wording;
        if (!backorder.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + backorder + "</div>");
    }
}
