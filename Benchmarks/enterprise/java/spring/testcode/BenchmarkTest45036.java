// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest45036 {

    @PostMapping(path="/BenchmarkTest45036", consumes="text/plain")
    public void BenchmarkTest45036(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        byte[] raw = rawData.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String data = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
        new java.io.File(data).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
