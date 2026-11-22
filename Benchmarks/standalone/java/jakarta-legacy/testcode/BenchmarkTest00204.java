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
public class BenchmarkTest00204 {

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

    static final class FormData {
        private final String payload;
        FormData(String payload) { this.payload = payload; }
        String getPayload() { return payload; }
    }

    @GET
    @Path("/BenchmarkTest00204")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00204(@javax.validation.constraints.Size(max = 4096) @HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        FormData payload = new FormData(headerValue);
        String data = payload.getPayload();
        long randValue = java.util.concurrent.ThreadLocalRandom.current().nextLong() ^ data.hashCode();
        response.setHeader("X-Rand", String.valueOf(randValue));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
