// SPDX-License-Identifier: Apache-2.0
package com.example.anomalyscorer;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderSchedule {


    @PostMapping("/RenderSchedule")
    public void renderSchedule(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String caption = java.util.Optional.ofNullable(commentText).orElse("");
        String cohort = caption.replace("\u0000", "");
        response.getWriter().print("<div>" + cohort + "</div>");
    }
}
