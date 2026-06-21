// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest48523 {

    @GET
    @Path("/BenchmarkTest48523/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest48523(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = java.net.URLDecoder.decode(pathValue, "UTF-8");
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
