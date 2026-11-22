// SPDX-License-Identifier: Apache-2.0
package com.example.syndicationfeed;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.*;

@RestController
class AnnotateIndex {


    @PostMapping(path="/AnnotateIndex", consumes="multipart/form-data")
    public void annotateIndex(@javax.validation.constraints.Size(max = 4096) @RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = multipartField != null ? multipartField : "";
        java.util.Properties holder = new java.util.Properties();
        holder.setProperty("value", transcript);
        String addendum = holder.getProperty("value", "");
        byte[] serBytes = java.util.Base64.getDecoder().decode(addendum);
        try (ObjectInputStream ois = new ObjectInputStream(new java.io.ByteArrayInputStream(serBytes))) {
            Object obj = ois.readObject();
            response.setHeader("X-Deserialized-Class", obj != null ? obj.getClass().getName() : "null");
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
