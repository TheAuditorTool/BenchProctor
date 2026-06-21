// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest68377 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest68377")
    public void BenchmarkTest68377(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        String data = stripWhitespace(envValue);
        request.setAttribute("hidden_form_field", data);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
