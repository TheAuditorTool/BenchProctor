// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest65657 {

    @PostMapping("/BenchmarkTest65657")
    public void BenchmarkTest65657(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = "" + fieldValue;
        java.io.File listingDir = new java.io.File("/var/www/uploads");
        java.io.File[] entries = listingDir.listFiles();
        if (entries != null) {
            for (java.io.File listedFile : entries) {
                response.getWriter().println(listedFile.getName());
            }
        }
    }
}
