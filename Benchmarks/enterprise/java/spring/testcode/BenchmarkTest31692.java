// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest31692 {

    private static String normalize(String v) { return v.strip(); }
    private enum AllowedValue { PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED }

    @GetMapping("/BenchmarkTest31692")
    public void BenchmarkTest31692(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = normalize(userId);
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        response.setContentType("application/json");
        response.getWriter().print("{\"echo\":\"" + data + "\"}");
    }
}
