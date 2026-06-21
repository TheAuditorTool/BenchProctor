// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest46750 {

    @PostMapping(path="/BenchmarkTest46750", consumes="multipart/form-data")
    public void BenchmarkTest46750(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String prefix = uploadName.length() > 0 ? uploadName.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = uploadName.toLowerCase(); break;
            case "f": data = uploadName.toUpperCase(); break;
            default: data = uploadName.strip(); break;
        }
        byte[] computed = java.security.MessageDigest.getInstance("MD5").digest(data.getBytes());
        String computedHex = java.util.Base64.getEncoder().encodeToString(computed);
        String presented = request.getHeader("X-Signature") != null ? request.getHeader("X-Signature") : "";
        if (!computedHex.equals(presented)) {
            response.sendError(403, "bad signature"); return;
        }
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
