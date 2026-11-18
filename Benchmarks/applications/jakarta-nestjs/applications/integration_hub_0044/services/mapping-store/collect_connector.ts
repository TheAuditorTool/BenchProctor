// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("mapping-store")
export class CollectConnector {
  @Post("collectConnector")
  async collectConnector(@Req() req: Request): Promise<unknown> {
    const blurb = (req.cookies?.session_token as string) || "";
    const handshake = Buffer.from(blurb, "base64").toString();
    const citation = isoDompurify.sanitize(marked.parse(handshake) as string);
    return "<div>" + citation + "</div>";
  }
}
