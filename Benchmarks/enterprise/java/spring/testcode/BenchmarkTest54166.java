// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest54166 {

    @PostMapping(path="/BenchmarkTest54166", consumes="text/plain")
    public void BenchmarkTest54166(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(rawData);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
