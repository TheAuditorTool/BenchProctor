// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("survey-service")
export class RenderTicket {
  @Post("renderTicket")
  async renderTicket(@Req() req: Request): Promise<unknown> {
    const phrase = (req.query.id as string) || "";
    return "<div>" + phrase + "</div>";
  }
}
