// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest35179 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest35179", consumes="text/plain")
    public void BenchmarkTest35179(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = stripWhitespace(rawData);
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
