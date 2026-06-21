// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60064 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest60064.class);

    @GetMapping("/BenchmarkTest60064")
    public void BenchmarkTest60064(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String prefix = cookieValue.length() > 0 ? cookieValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = cookieValue.toLowerCase(); break;
            case "f": data = cookieValue.toUpperCase(); break;
            default: data = cookieValue.strip(); break;
        }
        LOG.info("request processed");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
