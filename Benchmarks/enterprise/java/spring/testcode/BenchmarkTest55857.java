// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest55857 {

    @GetMapping("/BenchmarkTest55857")
    public void BenchmarkTest55857(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "AKIAIOSFODNN7EXAMPLE";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + secretValue;
        String data = valueSupplier.get();
        URL url = java.net.URI.create("https://api.acmecdn.net/v1/data").toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestProperty("Authorization", "Bearer " + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
