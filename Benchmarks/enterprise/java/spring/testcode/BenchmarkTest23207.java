// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest23207 {

    @PostMapping(path="/BenchmarkTest23207", consumes="text/plain")
    public void BenchmarkTest23207(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        new java.io.File(rawData).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
