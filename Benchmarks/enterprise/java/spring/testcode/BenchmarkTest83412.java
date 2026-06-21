// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest83412 {

    @GetMapping("/BenchmarkTest83412")
    public void BenchmarkTest83412(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        System.loadLibrary(cookieValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
