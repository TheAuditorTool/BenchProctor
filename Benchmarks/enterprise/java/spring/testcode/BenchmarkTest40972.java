// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest40972 {

    private static String normalize(String v) { return v.strip(); }
    private enum AllowedValue { ACTIVE, IDLE, EXPIRED, REVOKED }

    @GetMapping("/BenchmarkTest40972/{pathId}")
    public void BenchmarkTest40972(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = normalize(pathValue);
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        request.getSession().setAttribute("data", String.valueOf(data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
