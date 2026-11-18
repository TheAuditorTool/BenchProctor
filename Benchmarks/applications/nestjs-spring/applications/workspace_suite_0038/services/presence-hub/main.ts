import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { TrackPresence } from "./presence_track";
import { CompactSummary } from "./compact_summary";
import { NormalizeSnapshot } from "./normalize_snapshot";
import { PublishSchedule } from "./publish_schedule";
import { PublishConfig } from "./publish_config";
import { RenderCheckpoint } from "./render_checkpoint";
import { MergeHeader } from "./merge_header";
import { BuildDocument } from "./build_document";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, TrackPresence, CompactSummary, NormalizeSnapshot, PublishSchedule, PublishConfig, RenderCheckpoint, MergeHeader, BuildDocument],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
