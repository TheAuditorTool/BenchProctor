// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest74192 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest74192", consumes="text/plain")
    public void BenchmarkTest74192(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = normalize(rawData);
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
