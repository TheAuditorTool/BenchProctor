// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest32238 {

    private enum AllowedValue { PLAIN, MARKDOWN, HTML, TEXT }

    @GetMapping("/BenchmarkTest32238/{pathId}")
    public void BenchmarkTest32238(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = "" + pathValue;
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        response.getWriter().print("<div>" + data + "</div>");
    }
}
