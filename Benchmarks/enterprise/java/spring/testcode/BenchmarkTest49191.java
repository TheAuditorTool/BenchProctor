// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest49191 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @PostMapping(path="/BenchmarkTest49191", consumes="text/plain")
    public void BenchmarkTest49191(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = collapseWhitespace(rawData);
        if (System.currentTimeMillis() > 1000000000000L) {
            response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + data + "\">");
        }
    }
}
