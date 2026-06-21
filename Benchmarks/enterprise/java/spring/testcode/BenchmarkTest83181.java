// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest83181 {

    @GetMapping("/BenchmarkTest83181")
    public void BenchmarkTest83181(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data = cookieValue.isEmpty() ? "default" : cookieValue;
        request.setAttribute("hidden_form_field", data);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
