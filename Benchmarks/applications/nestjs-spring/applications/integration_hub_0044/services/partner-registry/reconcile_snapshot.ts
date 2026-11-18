// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("partner-registry")
export class ReconcileSnapshot {
  @Post("reconcileSnapshot")
  async reconcileSnapshot(@Req() req: Request): Promise<unknown> {
    const blurb = (req.headers.authorization as string) || "";
    const handshake = Buffer.from(blurb, "base64").toString();
    return "<div>" + handshake + "</div>";
  }
}
