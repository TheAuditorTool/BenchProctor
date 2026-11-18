// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("presence-service")
export class AnnotateSnapshot {
  @Post("annotateSnapshot")
  async annotateSnapshot(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.cookies?.session_token as string) || "";
    const bulletin = Buffer.from(paragraph, "base64").toString();
    const synopsis = isoDompurify.sanitize(marked.parse(bulletin) as string);
    return "<div>" + synopsis + "</div>";
  }
}
