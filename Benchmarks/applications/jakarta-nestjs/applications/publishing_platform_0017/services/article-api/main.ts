import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { DraftArticle } from "./article_draft";
import { AuditCheckpoint } from "./audit_checkpoint";
import { VerifyDigest } from "./verify_digest";
import { FetchHeader } from "./fetch_header";
import { RenderArticle } from "./render_article";
import { ResolveBatch } from "./resolve_batch";
import { AuditHeader } from "./audit_header";
import { RotateLedger } from "./rotate_ledger";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, DraftArticle, AuditCheckpoint, VerifyDigest, FetchHeader, RenderArticle, ResolveBatch, AuditHeader, RotateLedger],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
