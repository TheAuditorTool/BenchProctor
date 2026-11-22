// SPDX-License-Identifier: Apache-2.0
package com.example.escalationservice;
import org.springframework.web.bind.annotation.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class ValidateManifest {


    @PostMapping(path="/ValidateManifest", consumes="multipart/form-data")
    public void validateManifest(@jakarta.validation.constraints.Size(max = 4096) @RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String preface = multipartField != null ? multipartField : "";
        java.util.Properties container = new java.util.Properties();
        container.setProperty("value", preface);
        String grievance = container.getProperty("value", "");
        byte[] serBytes = java.util.Base64.getDecoder().decode(grievance);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
