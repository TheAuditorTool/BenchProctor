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
public class BenchmarkTest47324 {

    @POST
    @Path("/BenchmarkTest47324")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest47324(@FormParam("field") String field, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("\\s+", " ");
        String data = transform.apply(fieldValue);
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
