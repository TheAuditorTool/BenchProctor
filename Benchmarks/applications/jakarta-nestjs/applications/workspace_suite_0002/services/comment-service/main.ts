import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { PostComment } from "./comment_post";
import { LoadSnapshot } from "./load_snapshot";
import { ValidateConfig } from "./validate_config";
import { LoadDigest } from "./load_digest";
import { ReconcileSnapshot } from "./reconcile_snapshot";
import { ExportPolicy } from "./export_policy";
import { FetchComment } from "./fetch_comment";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PostComment, LoadSnapshot, ValidateConfig, LoadDigest, ReconcileSnapshot, ExportPolicy, FetchComment],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
