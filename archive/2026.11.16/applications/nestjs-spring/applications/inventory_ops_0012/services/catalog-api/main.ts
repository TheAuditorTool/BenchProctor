import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { LookupSku } from "./sku_lookup";
import { BuildReport } from "./build_report";
import { AnnotateAllocation } from "./annotate_allocation";
import { ReconcileConfig } from "./reconcile_config";
import { FormatManifest } from "./format_manifest";
import { RenderReport } from "./render_report";
import { SummarizeSummary } from "./summarize_summary";
import { SummarizeBatch } from "./summarize_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, LookupSku, BuildReport, AnnotateAllocation, ReconcileConfig, FormatManifest, RenderReport, SummarizeSummary, SummarizeBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
