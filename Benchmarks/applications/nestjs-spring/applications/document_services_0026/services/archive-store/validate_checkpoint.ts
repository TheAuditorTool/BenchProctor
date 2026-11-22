// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("archive-store")
export class ValidateCheckpoint {
  @Post("validateCheckpoint")
  async validateCheckpoint(@Req() req: Request): Promise<unknown> {
    const preface = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const addendum: string = transform(preface);
    const _clean = isoDompurify.sanitize(addendum);
    const dossier = _clean;
    return new StreamableFile(Buffer.from("<section>" + dossier + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
