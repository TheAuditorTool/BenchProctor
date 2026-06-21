// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest77360 {

    @GetMapping("/BenchmarkTest77360")
    public void BenchmarkTest77360(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        byte[] hexBytes = new byte[userId.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(userId.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String data = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
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
