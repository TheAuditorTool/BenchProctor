// SPDX-License-Identifier: Apache-2.0
package com.example.transcodeservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@RestController
class MergeIndex {


    @GetMapping("/MergeIndex")
    public void mergeIndex(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String notice = id != null ? id : "";
        byte[] hexBytes = new byte[notice.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(notice.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String rendition = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        com.fasterxml.jackson.databind.ObjectMapper objectMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        objectMapper.activateDefaultTyping(com.fasterxml.jackson.databind.jsontype.BasicPolymorphicTypeValidator.builder().allowIfBaseType(Object.class).build(), com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping.NON_FINAL);
        Object polymorphicObj = objectMapper.readValue(rendition, Object.class);
        response.setHeader("X-Deserialized-Class", polymorphicObj != null ? polymorphicObj.getClass().getName() : "null");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
