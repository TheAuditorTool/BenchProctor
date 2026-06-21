// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.attribute.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest56714 {

    @PostMapping(path="/BenchmarkTest56714", consumes="application/xml")
    public void BenchmarkTest56714(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        java.util.Set<java.nio.file.attribute.PosixFilePermission> perms = java.util.EnumSet.of(java.nio.file.attribute.PosixFilePermission.OWNER_READ, java.nio.file.attribute.PosixFilePermission.OWNER_WRITE);
        java.nio.file.Files.setPosixFilePermissions(java.nio.file.Paths.get("/var/app/secret"), perms);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
