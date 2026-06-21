// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest11814 {

    @POST
    @Path("/BenchmarkTest11814")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest11814(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : xmlValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        return Response.ok(String.valueOf(data), MediaType.TEXT_HTML).build();
    }
}
