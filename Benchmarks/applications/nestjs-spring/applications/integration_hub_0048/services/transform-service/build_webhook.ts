// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("transform-service")
export class BuildWebhook {
  @Post("buildWebhook")
  async buildWebhook(@Req() req: Request): Promise<unknown> {
    const citation = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(citation);
    const _clean = isoDompurify.sanitize(handshake);
    const heading = _clean;
    return new StreamableFile(Buffer.from("<section>" + heading + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
