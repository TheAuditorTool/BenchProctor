// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("share-service")
export class FormatComment {
  @Post("formatComment")
  async formatComment(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["user-agent"] as string) || "";
    let remark;
    try { remark = JSON.parse(preface).value || preface; }
    catch (e) { remark = preface; }
    JSON.parse(remark);
    return { created: true };
  }
}
