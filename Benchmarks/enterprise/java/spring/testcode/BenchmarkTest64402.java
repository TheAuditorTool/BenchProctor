// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64402 {

    @GetMapping("/BenchmarkTest64402")
    public void BenchmarkTest64402(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = "" + forwardedIp;
        String escaped = "\"" + data.replace("\"", "\"\"") + "\"";
        response.getWriter().print(escaped + ",data");
    }
}
