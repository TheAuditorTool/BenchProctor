// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest03377 {

    @GET
    @Path("/BenchmarkTest03377")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest03377(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = refererValue.isEmpty() ? "default" : refererValue;
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
