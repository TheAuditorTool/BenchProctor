// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("partner-registry")
export class RenderWindow {
  @Post("renderWindow")
  async renderWindow(@Req() req: Request): Promise<unknown> {
    const wording = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(wording);
    const _clean = isoDompurify.sanitize(handshake);
    const subject = _clean;
    return new StreamableFile(Buffer.from("<section>" + subject + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
