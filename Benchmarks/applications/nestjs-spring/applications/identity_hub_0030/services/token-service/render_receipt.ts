// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("token-service")
export class RenderReceipt {
  @Post("renderReceipt")
  async renderReceipt(@Req() req: Request): Promise<unknown> {
    const tagline = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const persona: string = transform(tagline);
    const _clean = isoDompurify.sanitize(persona);
    const note = _clean;
    return new StreamableFile(Buffer.from("<section>" + note + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
