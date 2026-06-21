// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest56058 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest56058.class);

    @GetMapping("/BenchmarkTest56058")
    public void BenchmarkTest56058(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data;
        if (cookieValue.length() > 256) { data = cookieValue.substring(0, 256); }
        else { data = cookieValue; }
        LOG.info("request processed");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
