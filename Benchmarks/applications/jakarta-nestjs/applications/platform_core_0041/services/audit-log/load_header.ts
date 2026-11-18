// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("audit-log")
export class LoadHeader {
  @Post("loadHeader")
  async loadHeader(@Req() req: Request): Promise<unknown> {
    const passage = (req.query.id as string) || "";
    return "<div>" + passage + "</div>";
  }
}
