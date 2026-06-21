// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest21899 {

    @GET
    @Path("/BenchmarkTest21899")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest21899(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        int divisor = Integer.parseInt(refererValue);
        if (divisor == 0) { return Response.status(400).build(); }
        int result = 100 / divisor;
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
