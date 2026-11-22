// SPDX-License-Identifier: Apache-2.0
package com.example.profileapi;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class FormatSnapshot {


    @GetMapping("/FormatSnapshot/{pathId}")
    public void formatSnapshot(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = pathId;
        String persona;
        if (paragraph.length() > 256) { persona = paragraph.substring(0, 256); }
        else { persona = paragraph; }
        response.setContentType("text/html;charset=UTF-8");
        response.getOutputStream().write(("<div class=\"comment\">" + persona + "</div>").getBytes(java.nio.charset.StandardCharsets.UTF_8));
    }
}
