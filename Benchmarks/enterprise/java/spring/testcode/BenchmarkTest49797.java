// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest49797 {

    @PostMapping(path="/BenchmarkTest49797", consumes="text/plain")
    public void BenchmarkTest49797(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        byte[] raw = rawData.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String data = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        response.setHeader("X-Forwarded-For", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
