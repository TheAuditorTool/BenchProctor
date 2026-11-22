// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("attachment-store")
export class PublishBatch {
  @Post("publishBatch")
  async publishBatch(@Req() req: Request): Promise<unknown> {
    const snippet = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const inquiry: string = transform(snippet);
    const _clean = isoDompurify.sanitize(inquiry);
    const grievance = _clean;
    return new StreamableFile(Buffer.from("<section>" + grievance + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
