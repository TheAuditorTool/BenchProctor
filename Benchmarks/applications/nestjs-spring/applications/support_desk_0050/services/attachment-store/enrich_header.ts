// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";

@Controller("attachment-store")
export class EnrichHeader {
  @Post("enrichHeader")
  async enrichHeader(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers["user-agent"] as string) || "";
    const inquiry = nodeUtil.format("%s", remark);
    return "<div>" + inquiry + "</div>";
  }
}
