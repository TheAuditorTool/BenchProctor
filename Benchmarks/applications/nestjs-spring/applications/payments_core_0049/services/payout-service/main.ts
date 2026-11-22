import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SchedulePayout } from "./payout_schedule";
import { RotateBundle } from "./rotate_bundle";
import { MergeMandate } from "./merge_mandate";
import { NormalizeIndex } from "./normalize_index";
import { EnrichHeader } from "./enrich_header";
import { EnrichConfig } from "./enrich_config";
import { ReconcileDigest } from "./reconcile_digest";
import { ResolveConfig } from "./resolve_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SchedulePayout, RotateBundle, MergeMandate, NormalizeIndex, EnrichHeader, EnrichConfig, ReconcileDigest, ResolveConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
