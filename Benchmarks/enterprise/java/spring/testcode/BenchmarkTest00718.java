// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00718 {

    @PostMapping(path="/BenchmarkTest00718", consumes="text/plain")
    public void BenchmarkTest00718(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        request.getSession().setAttribute("data", String.valueOf(rawData));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
