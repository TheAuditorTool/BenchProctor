// SPDX-License-Identifier: Apache-2.0
package com.example.ocrservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderConversion {


    @GetMapping("/RenderConversion/{pathId}")
    public void renderConversion(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String note = pathId;
        String addendum = java.net.URLDecoder.decode(note, java.nio.charset.StandardCharsets.UTF_8);
        String dossier = addendum.matches("^(plain|markdown|html|text)$") ? addendum : "plain";
        response.getWriter().print("<div>" + dossier + "</div>");
    }
}
