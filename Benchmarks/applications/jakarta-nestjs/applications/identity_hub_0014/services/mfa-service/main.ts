import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { VerifyMfa } from "./mfa_verify";
import { VerifyConfig } from "./verify_config";
import { ResolveBundle } from "./resolve_bundle";
import { LoadRecord } from "./load_record";
import { CollectReceipt } from "./collect_receipt";
import { ArchiveCheckpoint } from "./archive_checkpoint";
import { LoadDigest } from "./load_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, VerifyMfa, VerifyConfig, ResolveBundle, LoadRecord, CollectReceipt, ArchiveCheckpoint, LoadDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
