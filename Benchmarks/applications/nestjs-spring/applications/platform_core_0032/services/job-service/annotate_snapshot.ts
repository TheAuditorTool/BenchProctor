// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("job-service")
export class AnnotateSnapshot {
  @Post("annotateSnapshot")
  async annotateSnapshot(@Req() req: Request): Promise<unknown> {
    const remark = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const persona: string = transform(remark);
    const _clean = isoDompurify.sanitize(persona);
    const handshake = _clean;
    return new StreamableFile(Buffer.from("<section>" + handshake + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
