// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64693 {

    private static String normalize(String v) { return v.strip(); }
    private enum AllowedValue { PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED }

    @GetMapping("/BenchmarkTest64693")
    public void BenchmarkTest64693(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = normalize(hostValue);
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        response.setContentType("application/json");
        response.getWriter().print("{\"echo\":\"" + data + "\"}");
    }
}
