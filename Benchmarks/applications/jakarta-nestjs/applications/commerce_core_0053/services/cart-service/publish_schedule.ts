// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("cart-service")
export class PublishSchedule {
  @Post("publishSchedule")
  async publishSchedule(@Req() req: Request): Promise<unknown> {
    const memo = (req.cookies?.session_token as string) || "";
    const voucher = Buffer.from(memo, "base64").toString();
    const backorder = isoDompurify.sanitize(marked.parse(voucher) as string);
    return "<div>" + backorder + "</div>";
  }
}
