// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";

@Controller("macro-service")
export class NormalizeDigest {
  @Post("normalizeDigest")
  async normalizeDigest(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers["user-agent"] as string) || "";
    const inquiry = nodeUtil.format("%s", phrase);
    return "<div>" + inquiry + "</div>";
  }
}
