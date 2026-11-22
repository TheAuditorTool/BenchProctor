// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("signature-verifier")
export class AuditBatch {
  @Post("auditBatch")
  async auditBatch(@Req() req: Request): Promise<unknown> {
    const heading = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(heading);
    const _clean = isoDompurify.sanitize(handshake);
    const remark = _clean;
    return new StreamableFile(Buffer.from("<section>" + remark + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
