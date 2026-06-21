// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13561 {

    @PostMapping(path="/BenchmarkTest13561", consumes="text/plain")
    public void BenchmarkTest13561(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        int result = 100 / Integer.parseInt(rawData);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
