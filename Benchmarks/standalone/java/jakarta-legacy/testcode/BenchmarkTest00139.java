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
public class BenchmarkTest00139 {

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

    @POST
    @Path("/BenchmarkTest00139/comments")
    @Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00139(@javax.validation.constraints.Size(max = 4096) @FormParam("comment") String commentText, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        FormData payload = new FormData(commentValue);
        String data = payload.getPayload();
        try { Integer.parseInt(data); }
        catch (NumberFormatException e) { return Response.status(400).build(); }
        int boundedVal = Math.max(0, Math.min(Integer.parseInt(data), 1048576));
        int quantity = boundedVal;
        int orderTotalCents = quantity * 1250;
        if (orderTotalCents > 5_000_000) { return Response.status(422).entity("order exceeds credit limit").build(); }
        response.setHeader("X-Order-Total", String.valueOf(orderTotalCents));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
