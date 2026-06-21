// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest82349 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GetMapping("/BenchmarkTest82349")
    public void BenchmarkTest82349(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String stdinValue = java.util.Optional.ofNullable(new java.util.Scanner(System.in).nextLine()).orElse("");
        String data = stripCRLF(stdinValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        ProcessBuilder pb = new ProcessBuilder(new String[]{"sh", "-c", "echo " + processed});
        pb.redirectErrorStream(true);
        pb.start().waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
