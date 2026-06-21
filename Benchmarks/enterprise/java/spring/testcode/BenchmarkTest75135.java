// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75135 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @GetMapping("/BenchmarkTest75135/{pathId}")
    public void BenchmarkTest75135(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = collapseWhitespace(pathValue);
        if (System.currentTimeMillis() > 1000000000000L) {
            response.getWriter().print("<div>" + data + "</div>");
        }
    }
}
