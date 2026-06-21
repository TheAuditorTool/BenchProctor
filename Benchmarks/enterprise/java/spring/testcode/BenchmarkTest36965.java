// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36965 {

    @PostMapping("/BenchmarkTest36965")
    public void BenchmarkTest36965(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = commentValue.isEmpty() ? "default" : commentValue;
        java.io.File listingDir = new java.io.File("/var/www/uploads");
        java.io.File[] entries = listingDir.listFiles();
        if (entries != null) {
            for (java.io.File listedFile : entries) {
                response.getWriter().println(listedFile.getName());
            }
        }
    }
}
