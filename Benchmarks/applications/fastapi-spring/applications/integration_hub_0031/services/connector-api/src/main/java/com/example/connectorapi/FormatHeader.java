// SPDX-License-Identifier: Apache-2.0
package com.example.connectorapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FormatHeader {


    @GetMapping("/FormatHeader/{pathId}")
    public void formatHeader(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String snippet = pathId;
        String handshake;
        if (snippet.length() > 256) { handshake = snippet.substring(0, 256); }
        else { handshake = snippet; }
        response.getWriter().print("<div>" + handshake + "</div>");
    }
}
