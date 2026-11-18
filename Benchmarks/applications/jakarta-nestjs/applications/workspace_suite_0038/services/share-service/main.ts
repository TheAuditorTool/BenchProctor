import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { GrantShare } from "./share_grant";
import { AnnotateDigest } from "./annotate_digest";
import { RotateDigest } from "./rotate_digest";
import { ExportDigest } from "./export_digest";
import { FormatComment } from "./format_comment";
import { PruneSchedule } from "./prune_schedule";
import { FetchDigest } from "./fetch_digest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, GrantShare, AnnotateDigest, RotateDigest, ExportDigest, FormatComment, PruneSchedule, FetchDigest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
