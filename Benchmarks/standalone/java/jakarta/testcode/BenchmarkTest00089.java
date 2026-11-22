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
public class BenchmarkTest00089 {

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
    @Path("/BenchmarkTest00089")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00089(@jakarta.validation.constraints.Size(max = 4096) @HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        try { Integer.parseInt(originValue); }
        catch (NumberFormatException e) { return Response.status(400).build(); }
        var boundedVal = Math.max(0, Math.min(Integer.parseInt(originValue), 1048576));
        int quantity = boundedVal;
        int orderTotalCents = quantity * 1250;
        if (orderTotalCents > 5_000_000) { return Response.status(422).entity("order exceeds credit limit").build(); }
        response.setHeader("X-Order-Total", String.valueOf(orderTotalCents));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
