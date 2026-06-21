// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest65193 {

    @PostMapping(path="/BenchmarkTest65193", consumes="text/plain")
    public void BenchmarkTest65193(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(rawData);
        String data = envelope.toString();
        Cookie cookie = new Cookie("session", data);
        cookie.setMaxAge(86400);
        response.addCookie(cookie);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
