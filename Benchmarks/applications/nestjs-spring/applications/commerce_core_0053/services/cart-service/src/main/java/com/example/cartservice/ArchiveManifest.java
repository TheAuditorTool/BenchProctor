// SPDX-License-Identifier: Apache-2.0
package com.example.cartservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class ArchiveManifest {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/ArchiveManifest", consumes="text/plain")
    public void archiveManifest(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String memo = rawBody != null ? rawBody : "";
        String voucher = normalize(memo);
        if (!voucher.matches("^[a-zA-Z0-9 _.#%\\-]+$")) { response.sendError(400); return; }
        response.getWriter().print("<div>" + voucher + "</div>");
    }
}
