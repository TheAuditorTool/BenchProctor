// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02863 {

    @PostMapping(path="/BenchmarkTest02863", consumes="text/plain")
    public void BenchmarkTest02863(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + rawData;
        String data = valueSupplier.get();
        request.isUserInRole("ADMIN");
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
