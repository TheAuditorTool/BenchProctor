// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("presence-hub")
export class TrackPresence {
  @Post("trackPresence")
  async trackPresence(@Req() req: Request): Promise<unknown> {
    const transcript = req.body.workspace_payload || "";
    return "<div>" + transcript + "</div>";
  }
}
