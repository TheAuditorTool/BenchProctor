// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("sla-monitor")
export class AuditPolicy {
  @Post("auditPolicy")
  async auditPolicy(@Req() req: Request): Promise<unknown> {
    const preface = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const grievance: string = transform(preface);
    const _clean = isoDompurify.sanitize(grievance);
    const inquiry = _clean;
    return new StreamableFile(Buffer.from("<section>" + inquiry + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
