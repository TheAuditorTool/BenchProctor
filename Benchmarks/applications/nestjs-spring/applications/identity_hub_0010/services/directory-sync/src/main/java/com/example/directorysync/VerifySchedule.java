// SPDX-License-Identifier: Apache-2.0
package com.example.directorysync;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.multipart.MultipartFile;

@RestController
class VerifySchedule {


    @PostMapping(path="/VerifySchedule", consumes="multipart/form-data")
    public void verifySchedule(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String phrase = file != null ? file.getOriginalFilename() : "";
        java.util.Properties holder = new java.util.Properties();
        holder.setProperty("value", phrase);
        String persona = holder.getProperty("value", "");
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        safeMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = safeMapper.readTree(persona);
        response.getWriter().print(node.path("name").asText());
    }
}
