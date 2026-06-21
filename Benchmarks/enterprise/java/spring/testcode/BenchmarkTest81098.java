// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81098 {

    @GetMapping("/BenchmarkTest81098")
    public void BenchmarkTest81098(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data = String.join(" ", cookieValue.split("\\s+"));
        response.getWriter().print(String.valueOf(data));
    }
}
