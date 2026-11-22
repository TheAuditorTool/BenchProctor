import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { BuildManifest } from "./stream_manifest";
import { EnrichSchedule } from "./enrich_schedule";
import { LoadCaption } from "./load_caption";
import { ValidateBundle } from "./validate_bundle";
import { PrunePolicy } from "./prune_policy";
import { ArchiveRecord } from "./archive_record";
import { MergeReceipt } from "./merge_receipt";
import { FetchConfig } from "./fetch_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, BuildManifest, EnrichSchedule, LoadCaption, ValidateBundle, PrunePolicy, ArchiveRecord, MergeReceipt, FetchConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
