// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest09602 {

    @GET
    @Path("/BenchmarkTest09602/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest09602(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = String.join(" ", pathValue.split("\\s+"));
        return Response.ok("<div>" + data + "</div>", MediaType.TEXT_HTML).build();
    }
}
