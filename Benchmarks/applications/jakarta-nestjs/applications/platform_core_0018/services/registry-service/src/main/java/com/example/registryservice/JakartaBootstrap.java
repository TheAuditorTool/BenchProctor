package com.example.registryservice;

public class JakartaBootstrap {

    @javax.ws.rs.Path("/health")
    public static class HealthResource {
        @javax.ws.rs.GET
        public javax.ws.rs.core.Response health() {
            return javax.ws.rs.core.Response.ok("ok").build();
        }
    }

    public static void main(String[] args) throws Exception {
        java.util.Map<String, String> initParams = new java.util.HashMap<>();
        initParams.put(
            "jersey.config.server.provider.classnames",
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.registryservice.JakartaBootstrap$HealthResource,com.example.registryservice.AnnotateWindow,com.example.registryservice.CollectSchedule,com.example.registryservice.CompactRoster,com.example.registryservice.FormatReceipt,com.example.registryservice.MergeReport,com.example.registryservice.RegisterService,com.example.registryservice.RotateTenant,com.example.registryservice.SummarizeDigest");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
