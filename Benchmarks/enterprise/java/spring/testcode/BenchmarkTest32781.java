// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.attribute.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest32781 {

    @PostMapping(path="/BenchmarkTest32781", consumes="multipart/form-data")
    public void BenchmarkTest32781(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(uploadName);
        String data = normalizer.apply(uploadName);
        if (!data.matches("^[\\w\\s.,;:_/\\-=]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        String[] modeChoices = {"rwxrwxrwx", "rwxr-xr-x", "rw-rw-rw-", "rwxrwx---", "rw-r--r--", "rwxr-x---", "r--r--r--", "rwx------"};
        String modeStr = data.matches("^[rwx-]{9}$") ? data : modeChoices[Math.abs(data.hashCode()) % modeChoices.length];
        java.util.Set<java.nio.file.attribute.PosixFilePermission> perms = java.nio.file.attribute.PosixFilePermissions.fromString(modeStr);
        java.nio.file.Files.setPosixFilePermissions(java.nio.file.Paths.get("/var/app/secret"), perms);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
