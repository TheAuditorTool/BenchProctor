import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { OpenCase } from "./case_open";
import { CollectHeader } from "./collect_header";
import { NormalizeIndex } from "./normalize_index";
import { ResolveDigest } from "./resolve_digest";
import { AuditSummary } from "./audit_summary";
import { PublishProfile } from "./publish_profile";
import { PruneBatch } from "./prune_batch";
import { CollectProfile } from "./collect_profile";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, OpenCase, CollectHeader, NormalizeIndex, ResolveDigest, AuditSummary, PublishProfile, PruneBatch, CollectProfile],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
