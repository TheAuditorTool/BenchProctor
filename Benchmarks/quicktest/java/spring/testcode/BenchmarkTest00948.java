// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00948 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest00948", consumes="text/plain")
    public void BenchmarkTest00948(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = normalize(rawData);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
