import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { RunConversion } from "./convert_job";
import { RenderSnapshot } from "./render_snapshot";
import { CompactRoster } from "./compact_roster";
import { RenderConversion } from "./render_conversion";
import { CollectSnapshot } from "./collect_snapshot";
import { ArchiveBundle } from "./archive_bundle";
import { BuildManifest } from "./build_manifest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RunConversion, RenderSnapshot, CompactRoster, RenderConversion, CollectSnapshot, ArchiveBundle, BuildManifest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
