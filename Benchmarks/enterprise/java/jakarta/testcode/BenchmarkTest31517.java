// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest31517 {

    @POST
    @Path("/BenchmarkTest31517")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest31517(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        StringBuilder bundle = new StringBuilder();
        bundle.append(xmlValue);
        String data = bundle.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.setHeader("Refresh", "0; url=" + processed);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
