// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("thumbnail-service")
export class EnrichLedger {
  @Post("enrichLedger")
  async enrichLedger(@Req() req: Request): Promise<unknown> {
    const snippet = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const montage: string = transform(snippet);
    const _clean = isoDompurify.sanitize(montage);
    const rendition = _clean;
    return new StreamableFile(Buffer.from("<section>" + rendition + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
