// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest68798 {

    private enum AllowedValue { APPLICATION_JSON, TEXT_PLAIN, TEXT_HTML, APPLICATION_XML }

    @GET
    @Path("/BenchmarkTest68798")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest68798(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        try { AllowedValue.valueOf(uaValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { uaValue = AllowedValue.values()[0].name().toLowerCase(); }
        response.setHeader("X-Forwarded-For", uaValue);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
