// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73782 {

    @PostMapping(path="/BenchmarkTest73782", consumes="text/plain")
    public void BenchmarkTest73782(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        response.addCookie(new Cookie("session", rawData));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
