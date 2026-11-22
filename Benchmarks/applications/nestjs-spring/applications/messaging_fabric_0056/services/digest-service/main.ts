import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { RollDigest } from "./digest_roll";
import { CompactChannel } from "./compact_channel";
import { ResolveConfig } from "./resolve_config";
import { PruneSchedule } from "./prune_schedule";
import { RenderProfile } from "./render_profile";
import { LoadPolicy } from "./load_policy";
import { EnrichConfig } from "./enrich_config";
import { ArchiveConfig } from "./archive_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RollDigest, CompactChannel, ResolveConfig, PruneSchedule, RenderProfile, LoadPolicy, EnrichConfig, ArchiveConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
