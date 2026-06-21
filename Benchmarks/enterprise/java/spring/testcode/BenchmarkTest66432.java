// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest66432 {

    @PostMapping(path="/BenchmarkTest66432", consumes="text/plain")
    public void BenchmarkTest66432(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = String.format("payload=%s", rawData);
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
