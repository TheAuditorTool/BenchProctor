// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest82712 {

    @POST
    @Path("/BenchmarkTest82712")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest82712(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String data = xmlValue.replace("\u0000", "");
        response.sendRedirect(data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
