import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RunConversion } from "./convert_job";
import { AnnotateBundle } from "./annotate_bundle";
import { NormalizeSnapshot } from "./normalize_snapshot";
import { RotateReceipt } from "./rotate_receipt";
import { FetchThreshold } from "./fetch_threshold";
import { BuildCheckpoint } from "./build_checkpoint";
import { AnnotateHeader } from "./annotate_header";
import { ReconcileBundle } from "./reconcile_bundle";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RunConversion, AnnotateBundle, NormalizeSnapshot, RotateReceipt, FetchThreshold, BuildCheckpoint, AnnotateHeader, ReconcileBundle],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
