// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest39077 {

    @PostMapping(path="/BenchmarkTest39077", consumes="text/plain")
    public void BenchmarkTest39077(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = "" + rawData;
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException e) { response.sendError(400); return; }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
