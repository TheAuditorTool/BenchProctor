// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("artifact-store")
export class RotatePolicy {
  @Post("rotatePolicy")
  async rotatePolicy(@Req() req: Request): Promise<unknown> {
    const remark = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const note: string = transform(remark);
    const _clean = isoDompurify.sanitize(note);
    const phrase = _clean;
    return new StreamableFile(Buffer.from("<section>" + phrase + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
