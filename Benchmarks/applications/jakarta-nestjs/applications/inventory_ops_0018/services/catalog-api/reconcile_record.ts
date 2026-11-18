// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("catalog-api")
export class ReconcileRecord {
  @Post("reconcileRecord")
  async reconcileRecord(@Req() req: Request): Promise<unknown> {
    const transcript = (req.cookies?.session_token as string) || "";
    const backorder = Buffer.from(transcript, "base64").toString();
    const restock = isoDompurify.sanitize(marked.parse(backorder) as string);
    return "<div>" + restock + "</div>";
  }
}
