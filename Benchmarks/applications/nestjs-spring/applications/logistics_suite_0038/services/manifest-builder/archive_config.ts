// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("manifest-builder")
export class ArchiveConfig {
  @Post("archiveConfig")
  async archiveConfig(@Req() req: Request): Promise<unknown> {
    const wording = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const consignment: string = transform(wording);
    const _clean = isoDompurify.sanitize(consignment);
    const parcel = _clean;
    return new StreamableFile(Buffer.from("<section>" + parcel + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
