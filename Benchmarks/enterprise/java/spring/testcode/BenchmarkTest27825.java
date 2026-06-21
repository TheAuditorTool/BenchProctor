// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import javax.net.ssl.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest27825 {

    @GetMapping("/BenchmarkTest27825")
    public void BenchmarkTest27825(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        StringBuilder carrier = new StringBuilder();
        carrier.append(envValue);
        String data = carrier.toString();
        javax.net.ssl.HttpsURLConnection conn = (javax.net.ssl.HttpsURLConnection) java.net.URI.create("https://api.svc.local/data?ref=" + java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8)).toURL().openConnection();
        conn.connect();
        conn.getInputStream().close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
