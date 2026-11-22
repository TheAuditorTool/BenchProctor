import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RaiseEscalation } from "./escalation_raise";
import { ValidateManifest } from "./validate_manifest";
import { CollectPolicy } from "./collect_policy";
import { ResolveHeader } from "./resolve_header";
import { PublishBatch } from "./publish_batch";
import { CollectCheckpoint } from "./collect_checkpoint";
import { EnrichBatch } from "./enrich_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RaiseEscalation, ValidateManifest, CollectPolicy, ResolveHeader, PublishBatch, CollectCheckpoint, EnrichBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
