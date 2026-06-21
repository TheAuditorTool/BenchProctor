// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest73639 {

    @GET
    @Path("/BenchmarkTest73639/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest73639(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        return Response.ok("<input type=\"text\" name=\"q\" value=\"" + pathValue + "\">", MediaType.TEXT_HTML).build();
    }
}
