// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80378 {

    @PostMapping(path="/BenchmarkTest80378", consumes="multipart/form-data")
    public void BenchmarkTest80378(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(multipartValue)); }
        catch (NumberFormatException e) { data = multipartValue; }
        String routeResult = "unknown";
        switch (data) {
            case "retry": routeResult = "retry-handled"; break;
            case "abort": routeResult = "abort-handled"; break;
            default: routeResult = "fallback"; break;
        }
        response.setHeader("X-Route-Result", routeResult);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
