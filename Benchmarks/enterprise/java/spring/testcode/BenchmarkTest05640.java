// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05640 {

    @GetMapping("/BenchmarkTest05640")
    public void BenchmarkTest05640(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(headerValue, "http");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        response.getWriter().print(data + ",data\n");
    }
}
