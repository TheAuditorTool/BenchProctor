// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest43080 {

    @GET
    @Path("/BenchmarkTest43080/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest43080(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data = String.join(" ", pathValue.split("\\s+"));
        try {
            Integer.parseInt(data);
        } catch (Exception e) { }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
