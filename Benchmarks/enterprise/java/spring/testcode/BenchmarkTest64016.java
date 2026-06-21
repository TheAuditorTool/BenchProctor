// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64016 {

    @GetMapping("/BenchmarkTest64016")
    public void BenchmarkTest64016(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + uaValue + "\">");
    }
}
