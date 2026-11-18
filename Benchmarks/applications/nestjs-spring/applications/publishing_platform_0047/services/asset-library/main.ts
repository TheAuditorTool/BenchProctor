import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { AttachAsset } from "./asset_attach";
import { ReconcileRecord } from "./reconcile_record";
import { ArchiveSchedule } from "./archive_schedule";
import { ResolveCheckpoint } from "./resolve_checkpoint";
import { FetchRoster } from "./fetch_roster";
import { FormatManifest } from "./format_manifest";
import { ValidateBundle } from "./validate_bundle";
import { CompactRecord } from "./compact_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, AttachAsset, ReconcileRecord, ArchiveSchedule, ResolveCheckpoint, FetchRoster, FormatManifest, ValidateBundle, CompactRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
