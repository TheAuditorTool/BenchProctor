// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("syndication-feed")
export class PushSyndication {
  @Post("pushSyndication")
  async pushSyndication(@Req() req: Request): Promise<unknown> {
    const excerpt = req.body.publishing_payload || "";
    return "<div>" + excerpt + "</div>";
  }
}
