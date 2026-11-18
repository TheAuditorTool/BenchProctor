// SPDX-License-Identifier: Apache-2.0
package com.example.sessionstore;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.multipart.MultipartFile;

@RestController
class FormatCheckpoint {


    @PostMapping(path="/FormatCheckpoint", consumes="multipart/form-data")
    public void formatCheckpoint(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String paragraph = file != null ? file.getOriginalFilename() : "";
        java.util.Properties box = new java.util.Properties();
        box.setProperty("value", paragraph);
        String persona = box.getProperty("value", "");
        com.fasterxml.jackson.databind.ObjectMapper safeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        safeMapper.disable(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES);
        com.fasterxml.jackson.databind.JsonNode node = safeMapper.readTree(persona);
        response.getWriter().print(node.path("name").asText());
    }
}
