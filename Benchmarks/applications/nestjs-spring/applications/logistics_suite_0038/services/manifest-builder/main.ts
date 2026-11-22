import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { BuildManifest } from "./manifest_build";
import { SummarizeWindow } from "./summarize_window";
import { FetchCheckpoint } from "./fetch_checkpoint";
import { ResolveShipment } from "./resolve_shipment";
import { ArchiveConfig } from "./archive_config";
import { BuildCheckpoint } from "./build_checkpoint";
import { BuildBatch } from "./build_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, BuildManifest, SummarizeWindow, FetchCheckpoint, ResolveShipment, ArchiveConfig, BuildCheckpoint, BuildBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
