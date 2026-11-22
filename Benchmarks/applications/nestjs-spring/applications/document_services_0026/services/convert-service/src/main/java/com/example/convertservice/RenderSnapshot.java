// SPDX-License-Identifier: Apache-2.0
package com.example.convertservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class RenderSnapshot {


    @GetMapping("/RenderSnapshot")
    public void renderSnapshot(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = java.util.Optional.ofNullable(System.getenv("DOCUMENTS_INPUT_0026")).orElse("");
        String addendum;
        if (preface.length() > 256) { addendum = preface.substring(0, 256); }
        else { addendum = preface; }
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        objectMapper.activateDefaultTyping(com.fasterxml.jackson.databind.jsontype.BasicPolymorphicTypeValidator.builder().allowIfBaseType(Object.class).build(), com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping.NON_FINAL);
        Object polymorphicObj = objectMapper.readValue(addendum, Object.class);
        response.setHeader("X-Deserialized-Class", polymorphicObj != null ? polymorphicObj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
