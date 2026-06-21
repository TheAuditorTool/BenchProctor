// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.attribute.*;

@Path("/")
public class BenchmarkTest79729 {

    @GET
    @Path("/BenchmarkTest79729")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest79729(@HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = authHeader.replace("\u0000", "");
        String[] modeChoices = {"rwxrwxrwx", "rwxr-xr-x", "rw-rw-rw-", "rwxrwx---", "rw-r--r--", "rwxr-x---", "r--r--r--", "rwx------"};
        String modeStr = data.matches("^[rwx-]{9}$") ? data : modeChoices[Math.abs(data.hashCode()) % modeChoices.length];
        java.util.Set<java.nio.file.attribute.PosixFilePermission> perms = java.nio.file.attribute.PosixFilePermissions.fromString(modeStr);
        java.nio.file.Files.setPosixFilePermissions(java.nio.file.Paths.get("/var/app/secret"), perms);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
