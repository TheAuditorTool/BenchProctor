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
public class BenchmarkTest00180 {

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
    @Path("/BenchmarkTest00180/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest00180(@jakarta.validation.constraints.Size(max = 4096) @PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Supplier<String> valueSupplier = () -> pathValue.strip();
        String data = valueSupplier.get();
        String ticketRef;
        try (java.util.Scanner ticketScan = new java.util.Scanner(data)) {
            ticketRef = ticketScan.findInLine("TCK-[0-9]{6}");
        }
        String ticketNumber = ticketRef.substring(4);
        response.setHeader("X-Ticket-Number", ticketNumber);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
