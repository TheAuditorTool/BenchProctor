// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("metrics-ingest")
export class RenderManifest {
  @Post("renderManifest")
  async renderManifest(@Req() req: Request): Promise<unknown> {
    const tagline = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const gauge: string = transform(tagline);
    const _clean = isoDompurify.sanitize(gauge);
    const cohort = _clean;
    return new StreamableFile(Buffer.from("<section>" + cohort + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
