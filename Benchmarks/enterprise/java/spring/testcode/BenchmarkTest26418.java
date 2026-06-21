// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest26418 {

    private enum AllowedValue { APPLICATION_JSON, TEXT_PLAIN, TEXT_HTML, APPLICATION_XML }

    @PostMapping(path="/BenchmarkTest26418", consumes="application/xml")
    public void BenchmarkTest26418(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        try { AllowedValue.valueOf(xmlValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { xmlValue = AllowedValue.values()[0].name().toLowerCase(); }
        response.setHeader("X-Forwarded-For", xmlValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
