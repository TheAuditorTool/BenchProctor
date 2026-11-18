import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { BuildManifest } from "./manifest_build";
import { RotateWindow } from "./rotate_window";
import { ValidateSummary } from "./validate_summary";
import { PruneLabel } from "./prune_label";
import { ArchiveSnapshot } from "./archive_snapshot";
import { AnnotateRoster } from "./annotate_roster";
import { PruneConfig } from "./prune_config";
import { CompactWaybill } from "./compact_waybill";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, BuildManifest, RotateWindow, ValidateSummary, PruneLabel, ArchiveSnapshot, AnnotateRoster, PruneConfig, CompactWaybill],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
