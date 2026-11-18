import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { EnqueueTranscode } from "./transcode_job";
import { EnrichThreshold } from "./enrich_threshold";
import { MergeIndex } from "./merge_index";
import { FetchWindow } from "./fetch_window";
import { LoadPolicy } from "./load_policy";
import { PruneLedger } from "./prune_ledger";
import { FormatManifest } from "./format_manifest";
import { PruneDigest } from "./prune_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, EnqueueTranscode, EnrichThreshold, MergeIndex, FetchWindow, LoadPolicy, PruneLedger, FormatManifest, PruneDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
