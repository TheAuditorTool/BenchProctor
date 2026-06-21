// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest26237 {

    @PostMapping(path="/BenchmarkTest26237", consumes="text/plain")
    public void BenchmarkTest26237(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        byte[] buf = new byte[Integer.parseInt(rawData)];
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
