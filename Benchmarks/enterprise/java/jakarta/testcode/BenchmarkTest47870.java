// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest47870 {

    @GET
    @Path("/BenchmarkTest47870")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest47870(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", refererValue);
        String data = sw.toString();
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
