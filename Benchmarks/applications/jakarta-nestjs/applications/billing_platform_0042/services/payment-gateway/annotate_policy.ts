// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

@Controller("payment-gateway")
export class AnnotatePolicy {
  @Post("annotatePolicy")
  async annotatePolicy(@Req() req: Request): Promise<unknown> {
    const remark = (req.cookies?.session_token as string) || "";
    const remittance = Buffer.from(remark, "base64").toString();
    const dunning = isoDompurify.sanitize(marked.parse(remittance) as string);
    return "<div>" + dunning + "</div>";
  }
}
