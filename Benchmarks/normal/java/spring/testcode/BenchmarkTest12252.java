// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12252 {

    @GetMapping("/BenchmarkTest12252")
    public void BenchmarkTest12252(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = String.format("payload=%s", authHeader);
        java.io.File listingDir = new java.io.File("/var/www/uploads");
        java.io.File[] entries = listingDir.listFiles();
        if (entries != null) {
            for (java.io.File listedFile : entries) {
                response.getWriter().println(listedFile.getName());
            }
        }
    }
}
