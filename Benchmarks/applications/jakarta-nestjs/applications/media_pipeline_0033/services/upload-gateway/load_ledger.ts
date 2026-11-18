// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("upload-gateway")
export class LoadLedger {
  @Post("loadLedger")
  async loadLedger(@Req() req: Request): Promise<unknown> {
    const transcript = (req.cookies?.session_token as string) || "";
    const rendition = Buffer.from(transcript, "base64").toString();
    const montage = isoDompurify.sanitize(marked.parse(rendition) as string);
    return "<div>" + montage + "</div>";
  }
}
