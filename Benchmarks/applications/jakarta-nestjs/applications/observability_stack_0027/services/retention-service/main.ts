import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SweepRetention } from "./retention_sweep";
import { SummarizeManifest } from "./summarize_manifest";
import { CompactIndex } from "./compact_index";
import { ReconcileThreshold } from "./reconcile_threshold";
import { EnrichSchedule } from "./enrich_schedule";
import { RenderBundle } from "./render_bundle";
import { CollectSample } from "./collect_sample";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SweepRetention, SummarizeManifest, CompactIndex, ReconcileThreshold, EnrichSchedule, RenderBundle, CollectSample],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
