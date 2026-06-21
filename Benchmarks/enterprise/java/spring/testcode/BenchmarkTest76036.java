// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest76036 {

    @PostMapping(path="/BenchmarkTest76036", consumes="text/plain")
    public void BenchmarkTest76036(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        if (!rawData.isEmpty()) throw new IllegalArgumentException("invalid input: " + rawData);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
