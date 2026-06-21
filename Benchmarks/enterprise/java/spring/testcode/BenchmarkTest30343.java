// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest30343 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest30343/{pathId}")
    public void BenchmarkTest30343(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = normalize(pathValue);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
