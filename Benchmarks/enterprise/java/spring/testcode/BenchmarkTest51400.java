// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest51400 {

    @PostMapping(path="/BenchmarkTest51400", consumes="text/plain")
    public void BenchmarkTest51400(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        request.getSession().setMaxInactiveInterval(900);
        request.getSession().setAttribute("data", String.valueOf(rawData));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
