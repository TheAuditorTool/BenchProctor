import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RunScreening } from "./screening_run";
import { CollectBundle } from "./collect_bundle";
import { VerifyPolicy } from "./verify_policy";
import { ValidatePolicy } from "./validate_policy";
import { ExportBatch } from "./export_batch";
import { ResolveSnapshot } from "./resolve_snapshot";
import { PruneConfig } from "./prune_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RunScreening, CollectBundle, VerifyPolicy, ValidatePolicy, ExportBatch, ResolveSnapshot, PruneConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
