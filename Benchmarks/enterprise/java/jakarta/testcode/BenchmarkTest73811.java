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
public class BenchmarkTest73811 {

    @GET
    @Path("/BenchmarkTest73811/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest73811(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        StringBuilder payload = new StringBuilder();
        payload.append(pathValue);
        String data = payload.toString();
        String[] modeChoices = {"rwxrwxrwx", "rwxr-xr-x", "rw-rw-rw-", "rwxrwx---", "rw-r--r--", "rwxr-x---", "r--r--r--", "rwx------"};
        String modeStr = data.matches("^[rwx-]{9}$") ? data : modeChoices[Math.abs(data.hashCode()) % modeChoices.length];
        java.util.Set<java.nio.file.attribute.PosixFilePermission> perms = java.nio.file.attribute.PosixFilePermissions.fromString(modeStr);
        java.nio.file.Files.setPosixFilePermissions(java.nio.file.Paths.get("/var/app/secret"), perms);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
