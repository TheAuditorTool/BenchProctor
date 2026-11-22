import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { IndexMetadata } from "./metadata_index";
import { FetchProfile } from "./fetch_profile";
import { RotateReceipt } from "./rotate_receipt";
import { VerifyRecord } from "./verify_record";
import { EnrichRoster } from "./enrich_roster";
import { LoadThreshold } from "./load_threshold";
import { ResolveReceipt } from "./resolve_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, IndexMetadata, FetchProfile, RotateReceipt, VerifyRecord, EnrichRoster, LoadThreshold, ResolveReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
