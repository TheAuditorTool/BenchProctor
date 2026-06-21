// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest04667 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @GET
    @Path("/BenchmarkTest04667/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest04667(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = stripCRLF(pathValue);
        response.setContentType("text/html");
        return Response.ok(data, MediaType.TEXT_HTML).build();
    }
}
