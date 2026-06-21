// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64895 {

    @PostMapping(path="/BenchmarkTest64895", consumes="text/plain")
    public void BenchmarkTest64895(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(rawData)); }
        catch (NumberFormatException e) { data = rawData; }
        if ("https://app.acmecdn.net".equals(data)) response.setHeader("Access-Control-Allow-Origin", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
