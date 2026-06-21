// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.net.*;

@Path("/")
public class BenchmarkTest41121 {

    @POST
    @Path("/BenchmarkTest41121")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest41121(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String prefix = xmlValue.length() > 0 ? xmlValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = xmlValue.toLowerCase(); break;
            case "f": data = xmlValue.toUpperCase(); break;
            default: data = xmlValue.strip(); break;
        }
        new Socket(data, 80).close();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
