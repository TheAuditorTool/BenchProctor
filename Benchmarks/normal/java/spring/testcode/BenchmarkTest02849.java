// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02849 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest02849", consumes="text/plain")
    public void BenchmarkTest02849(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = normalize(rawData);
        response.sendError(500, data);
    }
}
