// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("presence-service")
export class UpdatePresence {
  @Post("updatePresence")
  async updatePresence(@Req() req: Request): Promise<unknown> {
    const transcript = req.body.messaging_payload || "";
    nodeSerialize.unserialize(transcript);
    return { created: true };
  }
}
