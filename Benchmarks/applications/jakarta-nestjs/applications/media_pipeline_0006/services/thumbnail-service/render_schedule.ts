// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("thumbnail-service")
export class RenderSchedule {
  @Post("renderSchedule")
  async renderSchedule(@Req() req: Request): Promise<unknown> {
    const passage = (req.cookies?.session_token as string) || "";
    const montage = Buffer.from(passage, "base64").toString();
    const rendition = isoDompurify.sanitize(marked.parse(montage) as string);
    return "<div>" + rendition + "</div>";
  }
}
