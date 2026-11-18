// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("shipping-api")
export class MergeSnapshot {
  @Post("mergeSnapshot")
  async mergeSnapshot(@Req() req: Request): Promise<unknown> {
    const transcript = (req.cookies?.session_token as string) || "";
    const parcel = Buffer.from(transcript, "base64").toString();
    const consignment = isoDompurify.sanitize(marked.parse(parcel) as string);
    return "<div>" + consignment + "</div>";
  }
}
