import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { InvokeConnector } from "./connector_invoke";
import { FormatDigest } from "./format_digest";
import { ArchiveConnector } from "./archive_connector";
import { LoadBatch } from "./load_batch";
import { CollectDigest } from "./collect_digest";
import { NormalizeWindow } from "./normalize_window";
import { FormatPolicy } from "./format_policy";
import { ResolveMapping } from "./resolve_mapping";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, InvokeConnector, FormatDigest, ArchiveConnector, LoadBatch, CollectDigest, NormalizeWindow, FormatPolicy, ResolveMapping],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
