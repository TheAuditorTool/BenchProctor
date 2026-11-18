// SPDX-License-Identifier: Apache-2.0
package com.example.knowledgeindex;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class CollectSummary {


    @GetMapping("/CollectSummary")
    public void collectSummary(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = xCustomHeader != null ? xCustomHeader : "";
        String inquiry;
        try { inquiry = String.valueOf(Integer.parseInt(phrase)); }
        catch (NumberFormatException e) { inquiry = phrase; }
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        objectMapper.activateDefaultTyping(com.fasterxml.jackson.databind.jsontype.BasicPolymorphicTypeValidator.builder().allowIfBaseType(Object.class).build(), com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping.NON_FINAL);
        Object polymorphicObj = objectMapper.readValue(inquiry, Object.class);
        response.setHeader("X-Deserialized-Class", polymorphicObj != null ? polymorphicObj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
