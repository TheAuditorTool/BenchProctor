// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("retry-service")
export class RenderWindow {
  @Post("renderWindow")
  async renderWindow(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.query.id as string) || "";
    return "<div>" + synopsis + "</div>";
  }
}
