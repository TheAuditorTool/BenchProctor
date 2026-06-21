// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest22034 {

    @GET
    @Path("/BenchmarkTest22034")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest22034(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        return Response.ok("<div>" + refererValue + "</div>", MediaType.TEXT_HTML).build();
    }
}
