// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14623 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest14623", consumes="text/plain")
    public void BenchmarkTest14623(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = stripWhitespace(rawData);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        request.setAttribute("hidden_form_field", processed);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
