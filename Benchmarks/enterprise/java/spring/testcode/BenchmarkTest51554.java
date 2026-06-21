// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest51554 {

    @PostMapping(path="/BenchmarkTest51554", consumes="text/plain")
    public void BenchmarkTest51554(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        response.setContentType("text/html");
        response.getWriter().print(rawData);
    }
}
