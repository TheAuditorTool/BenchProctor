// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import javax.xml.parsers.*;

@Path("/")
public class BenchmarkTest20361 {

    @GET
    @Path("/BenchmarkTest20361/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest20361(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String prefix = pathValue.length() > 0 ? pathValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = pathValue.toLowerCase(); break;
            case "f": data = pathValue.toUpperCase(); break;
            default: data = pathValue.strip(); break;
        }
        DocumentBuilderFactory.newInstance().newDocumentBuilder().parse(new org.xml.sax.InputSource(new java.io.StringReader(data)));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
