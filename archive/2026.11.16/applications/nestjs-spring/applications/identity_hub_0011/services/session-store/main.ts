import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { CreateSession } from "./session_create";
import { FormatRecord } from "./format_record";
import { PruneProfile } from "./prune_profile";
import { RotateManifest } from "./rotate_manifest";
import { FormatThreshold } from "./format_threshold";
import { ValidateManifest } from "./validate_manifest";
import { FetchPolicy } from "./fetch_policy";
import { NormalizeConfig } from "./normalize_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, CreateSession, FormatRecord, PruneProfile, RotateManifest, FormatThreshold, ValidateManifest, FetchPolicy, NormalizeConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
