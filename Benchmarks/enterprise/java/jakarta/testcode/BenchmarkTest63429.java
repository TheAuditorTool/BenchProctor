// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest63429 {

    @GET
    @Path("/BenchmarkTest63429")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest63429(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(originValue)); }
        catch (NumberFormatException e) { data = originValue; }
        return Response.ok("<input type=\"text\" name=\"q\" value=\"" + data + "\">", MediaType.TEXT_HTML).build();
    }
}
