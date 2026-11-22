// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.ws.rs.*;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.ws.rs.container.ContainerRequestContext;
import javax.ws.rs.container.ContainerRequestFilter;
import javax.ws.rs.ext.ExceptionMapper;
import javax.ws.rs.ext.Provider;

@Path("/")
@Produces(MediaType.APPLICATION_JSON)
public class BenchmarkTest00115 {

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

    private static String normalize(String v) { return v.strip(); }

    @GET
    @Path("/BenchmarkTest00115")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00115(@javax.validation.constraints.Size(max = 4096) @HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = normalize(hostValue);
        String cookieValue = java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8);
        javax.servlet.http.Cookie sessionCookie = new javax.servlet.http.Cookie("session", cookieValue);
        sessionCookie.setPath("/");
        sessionCookie.setSecure(true);
        sessionCookie.setHttpOnly(true);
        response.addCookie(sessionCookie);
        response.setHeader("Set-Cookie", response.getHeader("Set-Cookie") + "; SameSite=Strict");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
