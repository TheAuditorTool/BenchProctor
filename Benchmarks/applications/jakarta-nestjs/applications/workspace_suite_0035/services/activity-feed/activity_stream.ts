// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("activity-feed")
export class StreamActivity {
  @Post("streamActivity")
  async streamActivity(@Req() req: Request): Promise<unknown> {
    const note = req.body.workspace_payload || "";
    nodeSerialize.unserialize(note);
    return { created: true };
  }
}
