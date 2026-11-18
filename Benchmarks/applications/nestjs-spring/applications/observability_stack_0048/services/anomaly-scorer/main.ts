import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ScoreAnomaly } from "./anomaly_score";
import { RenderCheckpoint } from "./render_checkpoint";
import { BuildBundle } from "./build_bundle";
import { ValidateBundle } from "./validate_bundle";
import { ResolveBundle } from "./resolve_bundle";
import { EnrichConfig } from "./enrich_config";
import { MergeDigest } from "./merge_digest";
import { ResolveReport } from "./resolve_report";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ScoreAnomaly, RenderCheckpoint, BuildBundle, ValidateBundle, ResolveBundle, EnrichConfig, MergeDigest, ResolveReport],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
