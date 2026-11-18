// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("mfa-service")
export class LoadDigest {
  @Post("loadDigest")
  async loadDigest(@Req() req: Request): Promise<unknown> {
    const snippet = (req.cookies?.session_token as string) || "";
    const persona = Buffer.from(snippet, "base64").toString();
    const synopsis = isoDompurify.sanitize(marked.parse(persona) as string);
    return "<div>" + synopsis + "</div>";
  }
}
