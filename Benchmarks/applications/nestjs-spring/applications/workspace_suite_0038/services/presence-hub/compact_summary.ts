// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("presence-hub")
export class CompactSummary {
  @Post("compactSummary")
  async compactSummary(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.referer as string) || "";
    const remark = preface != null ? preface : '';
    const fileContent = fs.readFileSync("/var/app/data/" + remark, "utf8");
    return fileContent;
  }
}
