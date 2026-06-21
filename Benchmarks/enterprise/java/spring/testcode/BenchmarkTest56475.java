// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest56475 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest56475")
    public void BenchmarkTest56475(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = normalize(userId);
        URL url = java.net.URI.create("http://" + data).toURL();
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        try {
            conn.connect();
            conn.getInputStream().close();
        } finally { conn.disconnect(); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
