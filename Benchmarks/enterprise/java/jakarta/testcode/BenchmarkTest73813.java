// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest73813 {

    @POST
    @Path("/BenchmarkTest73813")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest73813(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(xmlValue, "cookie");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        return Response.ok("<input type=\"text\" name=\"q\" value=\"" + data + "\">", MediaType.TEXT_HTML).build();
    }
}
