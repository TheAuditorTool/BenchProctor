// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest50969 {

    private enum AllowedValue { PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED }

    @GET
    @Path("/BenchmarkTest50969")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest50969(@HeaderParam("X-Custom-Header") String xCustomHeader, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        try { AllowedValue.valueOf(headerValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { headerValue = AllowedValue.values()[0].name().toLowerCase(); }
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + headerValue + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
