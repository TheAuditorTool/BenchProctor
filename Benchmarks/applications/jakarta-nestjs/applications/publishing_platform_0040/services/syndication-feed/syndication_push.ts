// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("syndication-feed")
export class PushSyndication {
  @Post("pushSyndication")
  async pushSyndication(@Req() req: Request): Promise<unknown> {
    const subtitle = req.body.publishing_payload || "";
    nodeSerialize.unserialize(subtitle);
    return { created: true };
  }
}
