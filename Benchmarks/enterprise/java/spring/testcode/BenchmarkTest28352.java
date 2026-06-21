// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest28352 {

    private enum AllowedValue { CONFIG, DATA, INDEX, SCHEMA }

    @PostMapping(path="/BenchmarkTest28352", consumes="application/xml")
    public void BenchmarkTest28352(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        try { AllowedValue.valueOf(xmlValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { xmlValue = AllowedValue.values()[0].name().toLowerCase(); }
        Files.delete(Paths.get("/var/app/data/" + xmlValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
