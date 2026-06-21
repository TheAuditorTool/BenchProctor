// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03888 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @PostMapping(path="/BenchmarkTest03888", consumes="text/plain")
    public void BenchmarkTest03888(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = toLowerCase(rawData);
        response.setContentType("application/json");
        response.getWriter().print("{\"echo\":\"" + data + "\"}");
    }
}
