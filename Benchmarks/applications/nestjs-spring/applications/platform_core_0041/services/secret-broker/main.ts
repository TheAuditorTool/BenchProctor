import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { FetchSecret } from "./secret_fetch";
import { CollectRecord } from "./collect_record";
import { NormalizeFlag } from "./normalize_flag";
import { ArchiveDigest } from "./archive_digest";
import { ReconcileConfig } from "./reconcile_config";
import { PublishQuota } from "./publish_quota";
import { NormalizeRoster } from "./normalize_roster";
import { ResolveBatch } from "./resolve_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, FetchSecret, CollectRecord, NormalizeFlag, ArchiveDigest, ReconcileConfig, PublishQuota, NormalizeRoster, ResolveBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
