// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.nio.file.Files;
import java.nio.file.Paths;

@Path("/")
public class BenchmarkTest21008 {

    @GET
    @Path("/BenchmarkTest21008")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest21008(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = "" + refererValue;
        java.util.Set<String> allowed = java.util.Set.of("libapp", "libutils");
        if (!allowed.contains(data)) { return Response.status(403).build(); }
        String checkedPath = data;
        String libName = java.nio.file.Paths.get(checkedPath).getFileName().toString();
        java.util.Set<String> allowedLibs = java.util.Set.of("libapp", "libutils");
        if (!allowedLibs.contains(libName)) {
            return Response.status(403).entity("library not allowed").build();
        }
        System.loadLibrary(libName);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
