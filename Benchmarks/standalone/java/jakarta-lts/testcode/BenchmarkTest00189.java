// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.container.ContainerRequestContext;
import jakarta.ws.rs.container.ContainerRequestFilter;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00189 {

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
    @Path("/BenchmarkTest00189")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00189(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data = headerValue.isEmpty() ? "default" : headerValue;
        String cookieValue = java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8);
        jakarta.servlet.http.Cookie sessionCookie = new jakarta.servlet.http.Cookie("session", cookieValue);
        sessionCookie.setPath("/");
        sessionCookie.setSecure(true);
        sessionCookie.setHttpOnly(true);
        sessionCookie.setAttribute("SameSite", "Strict");
        response.addCookie(sessionCookie);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
