// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("retention-service")
export class LoadWindow {
  @Post("loadWindow")
  async loadWindow(@Req() req: Request): Promise<unknown> {
    const summary = (req.query.id as string) || "";
    return "<div>" + summary + "</div>";
  }
}
