// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("index-builder")
export class ExportWindow {
  @Post("exportWindow")
  async exportWindow(@Req() req: Request): Promise<unknown> {
    const footnote = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const addendum: string = transform(footnote);
    const _clean = isoDompurify.sanitize(addendum);
    const dossier = _clean;
    return new StreamableFile(Buffer.from("<section>" + dossier + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
