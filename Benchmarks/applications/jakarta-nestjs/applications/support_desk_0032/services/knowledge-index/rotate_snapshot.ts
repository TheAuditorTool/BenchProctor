// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("knowledge-index")
export class RotateSnapshot {
  @Post("rotateSnapshot")
  async rotateSnapshot(@Req() req: Request): Promise<unknown> {
    const note = (req.cookies?.session_token as string) || "";
    const inquiry = Buffer.from(note, "base64").toString();
    const grievance = isoDompurify.sanitize(marked.parse(inquiry) as string);
    return "<div>" + grievance + "</div>";
  }
}
