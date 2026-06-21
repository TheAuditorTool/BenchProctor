// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest43158 {

    @GetMapping("/BenchmarkTest43158")
    public void BenchmarkTest43158(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "app_display_name";
        java.util.List<String> tokens = java.util.Arrays.asList(secretValue.split(","));
        String data = String.join(",", tokens);
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
