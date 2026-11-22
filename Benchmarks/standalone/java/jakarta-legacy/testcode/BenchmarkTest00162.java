// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.validation.Valid;
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
public class BenchmarkTest00162 {
    private static class UserInput {
        @javax.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

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

    @POST
    @Path("/BenchmarkTest00162")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00162(@Valid UserInput req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        java.util.Properties store = new java.util.Properties();
        store.setProperty("value", jsonValue);
        String data = store.getProperty("value", "");
        try { Double.parseDouble(data); }
        catch (NumberFormatException e) { return Response.status(400).build(); }
        String boundedVal = data;
        java.util.Map<String, Object> sessionProfile = (java.util.Map<String, Object>) request.getSession().getAttribute("profile");
        if (sessionProfile == null) {
            sessionProfile = new java.util.concurrent.ConcurrentHashMap<>();
            request.getSession().setAttribute("profile", sessionProfile);
        }
        sessionProfile.putAll(java.util.Map.of("displayName", boundedVal));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
