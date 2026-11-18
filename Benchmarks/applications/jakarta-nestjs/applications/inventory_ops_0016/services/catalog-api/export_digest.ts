// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("catalog-api")
export class ExportDigest {
  @Post("exportDigest")
  async exportDigest(@Req() req: Request): Promise<unknown> {
    const citation = (req.cookies?.session_token as string) || "";
    const backorder = Buffer.from(citation, "base64").toString();
    const restock = isoDompurify.sanitize(marked.parse(backorder) as string);
    return "<div>" + restock + "</div>";
  }
}
