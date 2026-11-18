// SPDX-License-Identifier: Apache-2.0
package com.example.shareservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FormatComment {


    @GetMapping("/FormatComment")
    public void formatComment(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = xForwardedFor != null ? xForwardedFor : "";
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(preface, "body");
        String remark = kv.getKey();
        if (!remark.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + remark + "</div>");
    }
}
