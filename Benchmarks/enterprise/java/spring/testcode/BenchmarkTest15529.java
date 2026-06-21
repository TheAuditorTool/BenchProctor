// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15529 {

    @GetMapping("/BenchmarkTest15529")
    public void BenchmarkTest15529(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "default_config_label";
        String data = "[%s]".formatted(secretValue);
        if (data == null) throw new IllegalArgumentException("input required");
        String envSecret = System.getenv("APP_SECRET");
        if (envSecret == null) throw new IllegalStateException("APP_SECRET unset");
        String storeCred = envSecret;
        URL url = java.net.URI.create("https://api.acmecdn.net/v1/data").toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestProperty("Authorization", "Bearer " + storeCred);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
