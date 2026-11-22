// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.Cookie;
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
public class BenchmarkTest00233 {

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
    @Path("/BenchmarkTest00233")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00233(@javax.validation.constraints.Size(max = 4096) @HeaderParam("Authorization") String authorization, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String cookieValue = java.net.URLEncoder.encode(authHeader, java.nio.charset.StandardCharsets.UTF_8);
        response.addHeader("Set-Cookie", "session=" + cookieValue + "; Path=/; HttpOnly; SameSite=Strict");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
