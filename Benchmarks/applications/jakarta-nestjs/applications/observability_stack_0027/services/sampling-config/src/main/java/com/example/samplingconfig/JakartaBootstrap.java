package com.example.samplingconfig;

public class JakartaBootstrap {

    @jakarta.ws.rs.Path("/health")
    public static class HealthResource {
        @jakarta.ws.rs.GET
        public jakarta.ws.rs.core.Response health() {
            return jakarta.ws.rs.core.Response.ok("ok").build();
        }
    }

    public static void main(String[] args) throws Exception {
        java.util.Map<String, String> initParams = new java.util.HashMap<>();
        initParams.put(
            "jersey.config.server.provider.classnames",
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.samplingconfig.JakartaBootstrap$HealthResource,com.example.samplingconfig.AnnotateReport,com.example.samplingconfig.CompactBatch,com.example.samplingconfig.ConfigureSample,com.example.samplingconfig.EnrichReceipt,com.example.samplingconfig.FetchConfig,com.example.samplingconfig.LoadBatch,com.example.samplingconfig.MergeReceipt,com.example.samplingconfig.RenderManifest");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
