// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import javax.xml.xpath.*;

@Path("/")
public class BenchmarkTest12822 {

    @GET
    @Path("/BenchmarkTest12822")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest12822(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        StringBuilder bundle = new StringBuilder();
        bundle.append(hostValue);
        String data = bundle.toString();
        if (!("true".equals(data) || "false".equals(data))) { return Response.status(400).build(); }
        XPathFactory xpf = XPathFactory.newInstance();
        XPath xpath = xpf.newXPath();
        xpath.evaluate("/users/user[@name='" + data + "']", new org.xml.sax.InputSource(new java.io.StringReader("<users/>")));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
