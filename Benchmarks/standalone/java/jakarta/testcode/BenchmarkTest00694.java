// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.nio.file.Files;
import java.nio.file.Paths;
import jakarta.ws.rs.container.ContainerRequestContext;
import jakarta.ws.rs.container.ContainerRequestFilter;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00694 {

    @Provider
    public static class BindingRestrictionFilter implements ContainerRequestFilter {
        @Override
        public void filter(ContainerRequestContext requestContext) {
            requestContext.getHeaders().remove("X-Internal-Bind");
        }
    }

    @Provider
    public static class FailureMapper implements ExceptionMapper<Exception> {
        @Override
        public Response toResponse(Exception ex) {
            return Response.status(500).entity("request failed").build();
        }
    }

    @GET
    @Path("/BenchmarkTest00694")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00694(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(originValue)); }
        catch (NumberFormatException e) { data = originValue; }
        java.util.Set<String> allowed = java.util.Set.of("config.json", "index.html");
        if (!allowed.contains(data)) { return Response.status(403).build(); }
        String checkedPath = "/var/app/data/" + data;
        Files.write(Paths.get(checkedPath), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
