// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest65902 {

    @GetMapping("/BenchmarkTest65902")
    public void BenchmarkTest65902(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        byte[] hexBytes = new byte[cookieValue.length() / 2];
        for (int hexIdx = 0; hexIdx < hexBytes.length; hexIdx++) {
            hexBytes[hexIdx] = (byte) Integer.parseInt(cookieValue.substring(hexIdx * 2, hexIdx * 2 + 2), 16);
        }
        String data = new String(hexBytes, java.nio.charset.StandardCharsets.UTF_8);
        System.loadLibrary(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
