import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SettleCapture } from "./capture_settle";
import { CompactHeader } from "./compact_header";
import { RotateThreshold } from "./rotate_threshold";
import { AnnotateCheckpoint } from "./annotate_checkpoint";
import { BuildConfig } from "./build_config";
import { ArchiveSchedule } from "./archive_schedule";
import { VerifyDigest } from "./verify_digest";
import { CollectIndex } from "./collect_index";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SettleCapture, CompactHeader, RotateThreshold, AnnotateCheckpoint, BuildConfig, ArchiveSchedule, VerifyDigest, CollectIndex],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
