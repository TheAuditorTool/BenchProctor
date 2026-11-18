import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { CollectTrace } from "./trace_collect";
import { ReconcileSnapshot } from "./reconcile_snapshot";
import { RotateBundle } from "./rotate_bundle";
import { LoadIndex } from "./load_index";
import { EnrichMetric } from "./enrich_metric";
import { RotateDigest } from "./rotate_digest";
import { VerifyReport } from "./verify_report";
import { RotateTrace } from "./rotate_trace";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, CollectTrace, ReconcileSnapshot, RotateBundle, LoadIndex, EnrichMetric, RotateDigest, VerifyReport, RotateTrace],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
