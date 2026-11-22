// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("signature-verifier")
export class EnrichReport {
  @Post("enrichReport")
  async enrichReport(@Req() req: Request): Promise<unknown> {
    const summary = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(summary);
    const _clean = isoDompurify.sanitize(handshake);
    const paragraph = _clean;
    return new StreamableFile(Buffer.from("<section>" + paragraph + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
