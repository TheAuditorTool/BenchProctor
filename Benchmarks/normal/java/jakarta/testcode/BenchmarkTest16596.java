// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest16596 {

    @GET
    @Path("/BenchmarkTest16596/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest16596(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data;
        try { data = String.valueOf(Integer.parseInt(pathValue)); }
        catch (NumberFormatException e) { data = pathValue; }
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + data + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
