// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest20952 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @PostMapping(path="/BenchmarkTest20952", consumes="text/plain")
    public void BenchmarkTest20952(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = toLowerCase(rawData);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        request.setAttribute("hidden_form_field", processed);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
