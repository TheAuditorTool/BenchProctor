// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("template-service")
export class NormalizeProfile {
  @Post("normalizeProfile")
  async normalizeProfile(@Req() req: Request): Promise<unknown> {
    const preface = (req.cookies?.session_token as string) || "";
    const bulletin = Buffer.from(preface, "base64").toString();
    const notice = isoDompurify.sanitize(marked.parse(bulletin) as string);
    return "<div>" + notice + "</div>";
  }
}
