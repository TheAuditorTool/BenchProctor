import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { StartRecovery } from "./recovery_start";
import { SummarizeBundle } from "./summarize_bundle";
import { MergeThreshold } from "./merge_threshold";
import { ResolveBatch } from "./resolve_batch";
import { ReconcileConfig } from "./reconcile_config";
import { PublishConfig } from "./publish_config";
import { RenderReport } from "./render_report";
import { ExportHeader } from "./export_header";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, StartRecovery, SummarizeBundle, MergeThreshold, ResolveBatch, ReconcileConfig, PublishConfig, RenderReport, ExportHeader],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
