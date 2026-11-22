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
public class BenchmarkTest00091 {

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
    @Path("/BenchmarkTest00091")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00091(@jakarta.validation.constraints.Size(max = 4096) @CookieParam("session_token") String sessionToken, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data = normalize(cookieValue);
        String setCookieValue = java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8);
        jakarta.servlet.http.Cookie sessionCookie = new jakarta.servlet.http.Cookie("session", setCookieValue);
        sessionCookie.setPath("/");
        sessionCookie.setSecure(true);
        sessionCookie.setHttpOnly(true);
        sessionCookie.setAttribute("SameSite", "Strict");
        response.addCookie(sessionCookie);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
