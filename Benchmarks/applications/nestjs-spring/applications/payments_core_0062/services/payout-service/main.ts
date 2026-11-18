import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SchedulePayout } from "./payout_schedule";
import { CollectReport } from "./collect_report";
import { CompactIndex } from "./compact_index";
import { EnrichDigest } from "./enrich_digest";
import { RenderBatch } from "./render_batch";
import { NormalizeSnapshot } from "./normalize_snapshot";
import { FormatManifest } from "./format_manifest";
import { BuildIndex } from "./build_index";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SchedulePayout, CollectReport, CompactIndex, EnrichDigest, RenderBatch, NormalizeSnapshot, FormatManifest, BuildIndex],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
