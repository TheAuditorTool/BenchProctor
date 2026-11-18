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
public class BenchmarkTest00708 {

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
    @Path("/BenchmarkTest00708")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00708(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.Properties box = new java.util.Properties();
        box.setProperty("value", authHeader);
        String data = box.getProperty("value", "");
        java.nio.file.Path baseName = java.nio.file.Paths.get(data).getFileName();
        String checkedPath = "/var/app/data/" + (baseName == null ? "index" : baseName.toString());
        Files.write(Paths.get(checkedPath), "data".getBytes());
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
