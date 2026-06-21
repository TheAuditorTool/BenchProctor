// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest23111 {

    @GetMapping("/BenchmarkTest23111")
    public void BenchmarkTest23111(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "app_display_name";
        String data = String.format("%s", secretValue);
        if (data == null) throw new IllegalArgumentException("input required");
        java.util.Properties props = new java.util.Properties();
        try (java.io.InputStream propsStream = new java.io.FileInputStream("/etc/app/credentials.properties")) {
            props.load(propsStream);
        }
        String storeCred = props.getProperty("api.key", "");
        URL url = java.net.URI.create("https://api.acmecdn.net/v1/data").toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestProperty("Authorization", "Bearer " + storeCred);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
