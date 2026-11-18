// SPDX-License-Identifier: Apache-2.0
package com.example.transcodeservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class EnrichThreshold {


    @PostMapping("/EnrichThreshold")
    public void enrichThreshold(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(notice, "cookie");
        String rendition = pair.getKey();
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        objectMapper.activateDefaultTyping(com.fasterxml.jackson.databind.jsontype.BasicPolymorphicTypeValidator.builder().allowIfBaseType(Object.class).build(), com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping.NON_FINAL);
        Object polymorphicObj = objectMapper.readValue(rendition, Object.class);
        response.setHeader("X-Deserialized-Class", polymorphicObj != null ? polymorphicObj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
