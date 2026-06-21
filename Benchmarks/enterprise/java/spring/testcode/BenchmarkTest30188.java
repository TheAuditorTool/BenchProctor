// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest30188 {

    @GetMapping("/BenchmarkTest30188")
    public void BenchmarkTest30188(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data = String.format("payload=%s", cookieValue);
        new java.io.File(data).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
