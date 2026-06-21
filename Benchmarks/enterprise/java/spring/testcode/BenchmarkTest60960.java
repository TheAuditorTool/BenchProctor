// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60960 {

    @GetMapping("/BenchmarkTest60960")
    public void BenchmarkTest60960(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = "" + originValue;
        response.setHeader("Refresh", "0; url=" + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
