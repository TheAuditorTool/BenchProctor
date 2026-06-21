// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest19653 {

    @PostMapping(path="/BenchmarkTest19653", consumes="text/plain")
    public void BenchmarkTest19653(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = rawData.isEmpty() ? "default" : rawData;
        response.addCookie(new Cookie("session", data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
