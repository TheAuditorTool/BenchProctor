// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeUtil from "util";

@Controller("session-store")
export class AnnotateSnapshot {
  @Post("annotateSnapshot")
  async annotateSnapshot(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers["user-agent"] as string) || "";
    const persona = nodeUtil.format("%s", paragraph);
    return "<div>" + persona + "</div>";
  }
}
