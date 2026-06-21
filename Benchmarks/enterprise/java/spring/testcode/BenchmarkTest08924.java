// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08924 {

    @GetMapping("/BenchmarkTest08924")
    public void BenchmarkTest08924(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        request.setAttribute("hidden_form_field", uaValue);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
